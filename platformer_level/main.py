import pygame, sys
from setting import *
from level import Level

#pygame_setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

#set name and game icon
pygame.display.set_caption('platform_logic')
new_icon = pygame.image.load('graphics/icon/icon.png').convert_alpha()
pygame.display.set_icon(new_icon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()  

    pygame.display.update()
    clock.tick(60)