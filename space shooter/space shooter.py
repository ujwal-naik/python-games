import pygame
import os
import time
import random
pygame.font.init()

WIDTH , HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Space Shooter")

# load images 
RED_SPACE_SHIP = pygame.image.load(os.path.join('Assets', 'pixel_ship_red_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('Assets', 'pixel_ship_green_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('Assets', 'pixel_ship_blue_small.png'))

# Player ship 
WHITE_SPACE_SHIP = pygame.image.load(os.path.join('Assets', 'pixel_white_ship.png'))

# lasers

RED_LASER = pygame.image.load(os.path.join('Assets','pixel_laser_red.png'))
GREEN_LASER = pygame.image.load(os.path.join('Assets','pixel_laser_green.png'))
BLUE_LASER = pygame.image.load(os.path.join('Assets','pixel_laser_blue.png'))
WHITE_LASER = pygame.image.load(os.path.join('Assets','pixel_laser_yellow.png'))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets','background-black.png')), (WIDTH,HEIGHT))

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 30)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0,0))

        # draw text
        level_label = main_font.render(f"Level: {level}", 1,(255,255,255))
        lives_label = main_font.render(f"Lives: {lives}", 1,(255,255,255))

        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH - level_label.get_width() - 10 ,10))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == '__main__':
    main()