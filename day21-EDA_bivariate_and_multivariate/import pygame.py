import pygame

pygame.init()

WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption('pong')

white = (255,255,255)
black = (0,0,0)\

padle_width = 10
padle_height = 100

left_padel = pygame.Rect(30,HEIGHT // 2 - 50, padle_width,padle_height)
right_padel = pygame.Rect(WIDTH-40,HEIGHT // 2-50,padle_width,padle_height)

padle_speed = 6
ball_size = 15
ball = pygame.Rect(WIDTH // 2, HEIGHT //2,)