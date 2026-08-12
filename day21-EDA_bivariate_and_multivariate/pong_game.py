import sys
import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
left_paddle = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
PADDLE_SPEED = 6

# Ball dimensions & physics
BALL_SIZE = 12
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Scores & Font setup
left_score = 0
right_score = 0
font = pygame.font.SysFont("Consolas", 40)


def reset_ball():
    """Resets the ball to the center and reverses launch direction."""
    global ball_speed_x, ball_speed_y
    ball.x = WIDTH // 2 - BALL_SIZE // 2
    ball.y = HEIGHT // 2 - BALL_SIZE // 2
    ball_speed_x *= -1  # Send ball toward the player who just scored
    ball_speed_y = 5


# Game Loop
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            pygame.quit()
            sys.exit()

    # 2. Key Controls (Smooth Movement)
    keys = pygame.key.get_pressed()

    # Left Paddle (W / S keys)
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Right Paddle (UP / DOWN arrows)
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # 3. Ball Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball Collision: Top & Bottom Walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball Collision: Paddles
    if ball.colliderect(left_paddle) and ball_speed_x < 0:
        ball_speed_x *= -1
    if ball.colliderect(right_paddle) and ball_speed_x > 0:
        ball_speed_x *= -1

    # 4. Scoring Logic
    if ball.left <= 0:
        right_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

    # 5. Drawing Elements
    screen.fill(BLACK)

    # Center dotted line
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Paddles and Ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Render Scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width(), 20))

    # Refresh Screen
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS