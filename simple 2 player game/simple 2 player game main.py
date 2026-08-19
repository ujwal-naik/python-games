import pygame
import os
import time
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255,250,250)
BLACK = (0,0,0)
ORANGE = (255,95,21)

pygame.display.set_caption("Simple 2 Player Game")



HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)


BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

FPS = 90
VELOCITY = 5

BULLET_VELOCITY =10
MAX_BULLET = 3

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets','Grenade.mp3'))
BULLET_SOUND = pygame.mixer.Sound(os.path.join('Assets','GunSilencer.mp3'))

SPACSHIP_WIDTH, SPACESHIP_HEIGHT = 55, 50

BLACK_SPACESHIP_IMAGE= pygame.image.load(os.path.join("Assets", "black_spaceship.png"))
BLACK_SPACESHIP = pygame.transform.rotate(BLACK_SPACESHIP_IMAGE, 270)  # Rotate the black spaceship by 90 degrees
BLACK_SPACESHIP_SIZE = pygame.transform.scale(BLACK_SPACESHIP, (SPACSHIP_WIDTH, SPACESHIP_HEIGHT))  # Scale the black spaceship to the desired size

ORANGE_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "orange_spaceship.png"))
ORANGE_SPACESHIP = pygame.transform.rotate(ORANGE_SPACESHIP_IMAGE, 90)  # Rotate the orange spaceship by 270 degrees
ORANGE_SPACESHIP_SIZE = pygame.transform.scale(ORANGE_SPACESHIP, (SPACSHIP_WIDTH, SPACESHIP_HEIGHT))  # Scale the orange spaceship to the desired size

BLACK_HIT = pygame.USEREVENT + 1
ORANGE_HIT = pygame.USEREVENT + 2

def draw_window(black, orange, black_bullets, orange_bullets, orange_health, black_health):
    WIN.fill((100, 100, 100))  # Fill the window with black color
    pygame.draw.rect(WIN,WHITE,BORDER)

    black_health_text = HEALTH_FONT.render("Health: " + str(black_health), 1, WHITE)
    orange_health_text = HEALTH_FONT.render("Health: " + str(orange_health), 1, WHITE)
    WIN.blit(black_health_text, (WIDTH - black_health_text.get_width() -10 , 10))
    WIN.blit(orange_health_text, (10 , 10))
        
    WIN.blit(BLACK_SPACESHIP_SIZE, (black.x, black.y))  # Draw the black spaceship
    WIN.blit(ORANGE_SPACESHIP_SIZE, (orange.x, orange.y))  # Draw the orange spaceship  

    for bullet in black_bullets:
        pygame.draw.rect(WIN,BLACK,bullet)

    for bullet in orange_bullets :
        pygame.draw.rect(WIN,ORANGE,bullet)

    pygame.display.update()  # Update the display


def orange_handle_movement(keys_pressed,orange):
    if keys_pressed[pygame.K_LEFT] and orange.x - VELOCITY > BORDER.x:
        orange.x -= VELOCITY                                                     # left
    if keys_pressed[pygame.K_RIGHT] and orange.x + VELOCITY+ orange.width < WIDTH:
        orange.x += VELOCITY                                                     # right
    if keys_pressed[pygame.K_UP] and orange.y - VELOCITY > 0:
        orange.y -= VELOCITY                                                     # up
    if keys_pressed[pygame.K_DOWN] and orange.y + VELOCITY + orange.height <   HEIGHT:
        orange.y += VELOCITY                                                     # down

def black_handle_maovment(keys_pressed,black):
    if keys_pressed[pygame.K_a] and black.x - VELOCITY > 0:
        black.x -= VELOCITY                                                     # Move the orange spaceship left
    if keys_pressed[pygame.K_d] and black.x + VELOCITY + black.width < BORDER.x:
        black.x += VELOCITY                                                     # Move the orange spaceship right
    if keys_pressed[pygame.K_w] and black.y - VELOCITY > 0:
        black.y -= VELOCITY                                                     # Move the orange spaceship up
    if keys_pressed[pygame.K_s] and black.y + VELOCITY + black.height <   HEIGHT:
        black.y += VELOCITY                                                     # Move the orange spaceship down

def handle_bullets(black_bullets, orange_bullets, black, orange):
    for bullet in orange_bullets:
        bullet.x -= BULLET_VELOCITY 
        if black.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLACK_HIT))
            orange_bullets.remove(bullet)
        elif bullet.x < 0:
            orange_bullets.remove(bullet)

    for bullet in black_bullets:
        bullet.x += BULLET_VELOCITY 
        if orange.colliderect(bullet):
            pygame.event.post(pygame.event.Event(ORANGE_HIT))
            black_bullets.remove(bullet)
        elif bullet.x > WIDTH :
            black_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text , 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2 ))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    black = pygame.Rect(100, 300, SPACSHIP_WIDTH, SPACESHIP_HEIGHT)
    orange = pygame.Rect(600, 300, SPACSHIP_WIDTH, SPACESHIP_HEIGHT)

    black_bullets = []
    orange_bullets = []

    black_health = 10
    orange_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)  # Limit the frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL  and len(black_bullets) < MAX_BULLET:
                    bullet = pygame.Rect(black.x + black.width,black.y + black.height //2 - 2, 10 ,5)
                    black_bullets.append(bullet)
                    BULLET_SOUND.play()

                if event.key == pygame.K_RCTRL  and  len(orange_bullets) < MAX_BULLET:
                    bullet = pygame.Rect(orange.x , orange.y + orange.height //2 - 2, 10 ,5)
                    orange_bullets.append(bullet)
                    BULLET_SOUND.play()

            if event.type == ORANGE_HIT:
                black_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type ==  BLACK_HIT:
                orange_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if orange_health <= 0:
            winner_text = "Orange wins"

        if black_health <= 0:
            winner_text = "black wins"

        if winner_text != "":
            draw_winner(winner_text)
            break

        print(black_bullets,orange_bullets)            
        keys_pressed = pygame.key.get_pressed()
        orange_handle_movement(keys_pressed,orange)
        black_handle_maovment(keys_pressed,black)
        
        handle_bullets(black_bullets, orange_bullets, black, orange)
        draw_window(black, orange, black_bullets, orange_bullets, orange_health, black_health )  # Call the draw function to update the window

    main()

if __name__ == "__main__":
    main()