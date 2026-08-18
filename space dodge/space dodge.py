import pygame
import random
import time

# -----------window properties-------------------
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
display = pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("space bg.jpg"), (WIDTH, HEIGHT))

# -----------player properties-------------------
PLAYER_WIDTH, PLAYER_HEIGHT = 30, 40
PLAYER_VELOCITY = 4

# ------------star properties-------------------
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VELOCITY = 3

# ------------font properties-------------------
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 30)

# -----------draw function---------------------

def draw(player, elapsed_time,stars):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, (255, 0, 0), player)

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (5, 10))

    for star in stars:
        pygame.draw.rect(WIN, (255, 255, 0), star)

    #Update the display after drawing everything
    pygame.display.update()   

#-----------main function---------------------

def main():
    run = True
    # -----------player properties-------------------
    player = pygame.Rect( 200,HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    # ------------time properties---------------------
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    # -----------star properties-------------------

    star_add_increment = 2000
    star_count = 0 

    stars = []
    Hit = False

    while run:
        # ------Update the star count based on the time elapsed since the last frame-----

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time 

        # ------Add new stars based on the elapsed time-----

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)

                # Create a new star rectangle and add it to the list of stars

                star = pygame.Rect(star_x,-STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)  #  "-STAR_HEIGHT" to start the star just above the screen
                stars.append(star)
            star_add_increment = max( 200,star_add_increment - 50)   # Decrease the interval between star additions
            star_count = 0

        # -----Handle events and player movement-----

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # -----------------Handle player movement based on key presses-----------------------

        keys = pygame.key.get_pressed()

        #-----Move the player left -----
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:  
            player.x -= PLAYER_VELOCITY 
        if keys[pygame.K_a] and player.x - PLAYER_VELOCITY >= 0:  
            player.x -= PLAYER_VELOCITY 

        #-----Move the player right -----
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH: 
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

        # ----- Draw everything on the screen after collision-----

        if Hit:
            lost_text = FONT.render(f"You lost! Time survived: {round(elapsed_time)}s", 1, (255, 255, 255))
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        draw(player, elapsed_time, stars)
    pygame.quit()

if __name__ == "__main__":
    main()