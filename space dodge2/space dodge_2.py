import os

import pygame
pygame.mixer.init()
import random
import time

# -----------window properties-------------------
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
display = pygame.display.set_caption("Space Dodge2")

BG = pygame.transform.scale(pygame.image.load("space bg.png"), (WIDTH, HEIGHT))
#-----------spaceship properties-------------------
SPACSHIP_WIDTH, SPACESHIP_HEIGHT = 55, 50
ORANGE_SPACESHIP_IMAGE = pygame.image.load(os.path.join("orange_spaceship.PNG"))
ORANGE_SPACESHIP = pygame.transform.rotate(ORANGE_SPACESHIP_IMAGE,0)  
ORANGE_SPACESHIP_SIZE = pygame.transform.scale(ORANGE_SPACESHIP, (SPACSHIP_WIDTH, SPACESHIP_HEIGHT))  # Scale the orange spaceship to the desired size

# -----------player properties-------------------
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 40
PLAYER_VELOCITY = 6
ORANGE_HIT = pygame.USEREVENT + 2

# ------------star properties-------------------
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3
STAR_HIT = pygame.USEREVENT + 1


#-------------bullet propeties -------------------
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Grenade.mp3'))
BULLET_SOUND = pygame.mixer.Sound(os.path.join('GunSilencer.mp3'))

BULLET_VELOCITY =5
MAX_BULLET = 3

# ------------font properties-------------------
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)

# -----------draw function---------------------

def draw(player, elapsed_time,stars,orange_bullets):
    WIN.blit(BG, (0, 0))

    # pygame.draw.rect(WIN, (255, 0, 0), player)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (5, 10))

    WIN.blit(ORANGE_SPACESHIP_SIZE, (player.x, player.y))  # Draw the orange spaceship

    for star in stars:
        pygame.draw.rect(WIN, (255, 255, 0), star)

    for bullet in orange_bullets :
        pygame.draw.rect(WIN,(255,0, 0),bullet)
    #Update the display after drawing everything
    pygame.display.update()   

def handle_bullets( orange_bullets, black, orange):
    for bullet in orange_bullets:
        bullet.x += BULLET_VELOCITY 
        if black.colliderect(bullet):
            pygame.event.post(pygame.event.Event(STAR_HIT))
            orange_bullets.remove(bullet)
        elif bullet.x < 0:
            orange_bullets.remove(bullet)

#-----------main function---------------------

def main():
    run = False
    # -----------player properties-------------------
    player = pygame.Rect(600, 300, SPACSHIP_WIDTH, SPACESHIP_HEIGHT)

    orange_bullets = []

    # ------------time properties---------------------
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    # -----------star properties-------------------

    star_add_increment = 2000
    star_count = 0 

    stars = []
    Hit = False

    keys = pygame.key.get_pressed()

    while not run:
        # ------Update the star count based on the time elapsed since the last frame-----

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if (event.type == pygame.KEYDOWN
                    and event.key == pygame.K_RCTRL
                    and len(orange_bullets) < MAX_BULLET):
                bullet = pygame.Rect(
                    player.right, player.centery - 2, 10, 5
                )
                orange_bullets.append(bullet)
                BULLET_SOUND.play()

        # ------Add new stars based on the elapsed time-----

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)

                # Create a new star rectangle and add it to the list of stars

                star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)  #  "-STAR_HEIGHT" to start the star just above the screen
                stars.append(star)
            star_add_increment = max( 200,star_add_increment - 50)   # Decrease the interval between star additions
            star_count = 0
        

        # -----------------Handle player movement based on key presses-----------------------
        keys = pygame.key.get_pressed()
        
        

        #-----Move the player left -----
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:  
            player.x -= PLAYER_VELOCITY 
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:  
            player.x -= PLAYER_VELOCITY 

        #-----Move the player right -----
        if keys[pygame.K_RIGHT ] and player.x + PLAYER_VELOCITY + player.width <= WIDTH: 
            player.x += PLAYER_VELOCITY
        if keys[pygame.K_d] and player.x + PLAYER_VELOCITY + player.width <= WIDTH: 
            player.x += PLAYER_VELOCITY

        #-----Move the player up -----
        if keys[pygame.K_UP] and player.y - PLAYER_VELOCITY >= 0:
            player.y -= PLAYER_VELOCITY
        if keys[pygame.K_w] and player.y - PLAYER_VELOCITY >= 0:  
            player.y -= PLAYER_VELOCITY 

        #-----Move the player down -----
        if keys[pygame.K_s] and player.y + PLAYER_VELOCITY + player.height <= HEIGHT:
            player.y += PLAYER_VELOCITY        
        if keys[pygame.K_DOWN] and player.y + PLAYER_VELOCITY + player.height <= HEIGHT:
            player.y += PLAYER_VELOCITY
        

        # -----Update star positions and check for collisions-----

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)                           # Remove stars that have moved off the bottom of the screen

            elif star.y + star.height >= player.y and star.colliderect(player):   # Check for collision with the player
                stars.remove(star)                                     
                Hit = True
                break
           
        for bullet in orange_bullets[:]:
            bullet.y -= BULLET_VELOCITY
            if bullet.left < 0:
                orange_bullets.remove(bullet)
        
        # ----- Draw everything on the screen after collision-----

        # ----- Handle Game Over State -----
        if Hit:
            lost_text = FONT.render(f"You lost! Time survived: {round(elapsed_time)}s", 1, (255, 255, 255))
            retry_text = FONT.render("Press R to retry or Q to quit", 1, (255, 255, 255))
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            WIN.blit(retry_text, (WIDTH/2 - retry_text.get_width()/2, HEIGHT/2 + retry_text.get_height()))
            pygame.display.update()

            # Wait for user input (Restart or Quit)
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            main()   # Restart the game loop fresh
                            return
                        if event.key == pygame.K_q:
                            pygame.quit()
                            return

        draw(player, elapsed_time, stars,orange_bullets)
            
if __name__ == "__main__":
    main()