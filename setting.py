import pygame
import sys

pygame.init()

screen_width = 960
screen_height = 540
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
speed = 5
p1_score = 0
p2_score = 0
i = 0
start = 0

background = pygame.image.load("background.jpg")

score_font = pygame.font.SysFont('mvboli', 50)
how_font = pygame.font.SysFont('mvboli', 30)
start_font = pygame.font.SysFont('lucidasans', 100)
end_font = pygame.font.SysFont('arial', 20)
countdown_font = pygame.font.SysFont('lucidasans', 200)

cross1 = pygame.image.load("cross1.png")
cross1.set_alpha(None)
cross1.set_colorkey((255, 255, 255))
cross2 = pygame.image.load("cross2.png")
cross2.set_alpha(None)
cross2.set_colorkey((255, 255, 255))

fly_image = pygame.image.load("fly.png")
dead_fly = pygame.image.load("dead_fly.png")
flies = []
dead_flies = []
fly_pos = [0, screen_width]

cross1_size = cross1.get_rect().size
cross2_size = cross2.get_rect().size

cross1_width = cross1_size[0]
cross1_height = cross1_size[1]
cross1_x_pos = screen_width / 3 - cross1_width / 2
cross1_y_pos = screen_height / 2 - cross1_height / 2

cross2_width = cross2_size[0]
cross2_height = cross2_size[1]
cross2_x_pos = screen_width / 3 * 2 - cross2_width / 2
cross2_y_pos = screen_height / 2 - cross2_height / 2

to_x1 = 0
to_y1 = 0
to_x2 = 0
to_y2 = 0