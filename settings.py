import pygame 
width, height = 600, 400
cell_size = 20
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game AI')

# FPS (frames per second) controller
clock = pygame.time.Clock()
speed = 10
