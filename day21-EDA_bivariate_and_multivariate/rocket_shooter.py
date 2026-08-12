import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Display Dimensions
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Retro Football Match")
clock = pygame.time.Clock()
FPS = 60

# Colors
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
RED = (220, 20, 60)
BLACK = (0, 0, 0)
GOAL_COLOR = (200, 200, 200)

# Field Dimensions
GOAL_HEIGHT = 160
GOAL_Y1 = (HEIGHT - GOAL_HEIGHT) // 2
GOAL_Y2 = GOAL_Y1 + GOAL_HEIGHT

class Ball:
    def __init__(self, x, y):
        self.reset(x, y)
        self.radius = 10

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def update(self):
        # Apply velocity and friction
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.98
        self.vy *= 0.98

        # Top/Bottom Wall Collisions
        if self.y - self.radius < 20:
            self.y = 20 + self.radius
            self.vy *= -1
        elif self.y + self.radius > HEIGHT - 20:
            self.y = HEIGHT - 20 - self.radius
            self.vy *= -1

        # Left/Right Outer Boundary Collisions (excluding Goal areas)
        if self.y < GOAL_Y1 or self.y > GOAL_Y2:
            if self.x - self.radius < 20:
                self.x = 20 + self.radius
                self.vx *= -1
            elif self.x + self.radius > WIDTH - 20:
                self.x = WIDTH - 20 - self.radius
                self.vx *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, BLACK, (int(self.x), int(self.y)), self.radius, 2)


class Player:
    def __init__(self, x, y, color, controls):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.color = color
        self.controls = controls
        self.radius = 18
        self.speed = 5

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y

    def handle_input(self, keys):
        dx, dy = 0, 0
        if keys[self.controls['up']]:
            dy -= 1
        if keys[self.controls['down']]:
            dy += 1
        if keys[self.controls['left']]:
            dx -= 1
        if keys[self.controls['right']]:
            dx += 1

        # Normalize diagonal movement
        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071

        self.x += dx * self.speed
        self.y += dy * self.speed

        # Keep player on pitch
        self.x = max(20 + self.radius, min(WIDTH - 20 - self.radius, self.x))
        self.y = max(20 + self.radius, min(HEIGHT - 20 - self.radius, self.y))

    def kick(self, ball):
        dx = ball.x - self.x
        dy = ball.y - self.y
        dist = math.hypot(dx, dy)

        # Elastic collision simulation
        if dist < self.radius + ball.radius:
            overlap = (self.radius + ball.radius) - dist
            if dist > 0:
                nx, ny = dx / dist, dy / dist
                ball.x += nx * overlap
                ball.y += ny * overlap
                
                # Transfer impulse to ball
                ball.vx += nx * 8
                ball.vy += ny * 8

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius, 2)


def draw_pitch():
    screen.fill(GREEN)
    
    # Outer boundaries
    pygame.draw.rect(screen, WHITE, (20, 20, WIDTH - 40, HEIGHT - 40), 4)
    
    # Halfway Line
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 20), (WIDTH // 2, HEIGHT - 20), 4)
    
    # Center Circle
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 70, 4)
    pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 6)

    # Goals Net Drawing
    # Left Goal
    pygame.draw.rect(screen, GOAL_COLOR, (0, GOAL_Y1, 20, GOAL_HEIGHT), 3)
    # Right Goal
    pygame.draw.rect(screen, GOAL_COLOR, (WIDTH - 20, GOAL_Y1, 20, GOAL_HEIGHT), 3)


# Setup Game Elements
p1_controls = {'up': pygame.K_w, 'down': pygame.K_s, 'left': pygame.K_a, 'right': pygame.K_d}
p2_controls = {'up': pygame.K_UP, 'down': pygame.K_DOWN, 'left': pygame.K_LEFT, 'right': pygame.K_RIGHT}

p1 = Player(150, HEIGHT // 2, BLUE, p1_controls)
p2 = Player(WIDTH - 150, HEIGHT // 2, RED, p2_controls)
ball = Ball(WIDTH // 2, HEIGHT // 2)

score_p1 = 0
score_p2 = 0
font = pygame.font.SysFont('arial', 36, bold=True)

# Main Loop
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Update Players & Ball
    p1.handle_input(keys)
    p2.handle_input(keys)

    p1.kick(ball)
    p2.kick(ball)
    
    ball.update()

    # Check for Goal scoring
    if ball.x - ball.radius < 5 and GOAL_Y1 < ball.y < GOAL_Y2:
        score_p2 += 1
        ball.reset(WIDTH // 2, HEIGHT // 2)
        p1.reset()
        p2.reset()
        pygame.time.delay(500)
    elif ball.x + ball.radius > WIDTH - 5 and GOAL_Y1 < ball.y < GOAL_Y2:
        score_p1 += 1
        ball.reset(WIDTH // 2, HEIGHT // 2)
        p1.reset()
        p2.reset()
        pygame.time.delay(500)

    # Drawing Elements
    draw_pitch()
    p1.draw(screen)
    p2.draw(screen)
    ball.draw(screen)

    # Scoreboard Overlay
    score_text = font.render(f"BLUE: {score_p1}   |   RED: {score_p2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 30))

    pygame.display.flip()