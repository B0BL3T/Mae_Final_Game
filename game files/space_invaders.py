import pygame
import sys
import random
import time
from math import atan2, pi
from player import Player
from parameters import *
from bullet import *
from bomb import *
from invader import *
from squad import *

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load the sound effects
hit_sound = pygame.mixer.Sound("../assets/sounds/enemy_explosion.mp3")  # invader killed
die_sound = pygame.mixer.Sound("../assets/sounds/player_die.mp3")  # player died
player_fire = pygame.mixer.Sound("../assets/sounds/default_shot.mp3")  # player fires
invader_bomb = pygame.mixer.Sound("../assets/sounds/torp_explosion.mp3")  # invader fires

'''bang = pygame.mixer.Sound('../assets/sounds/bang.wav')
tune = pygame.mixer.Sound("../assets/sounds/we_have_time.ogg")
# play background music
#pygame.mixer.Sound.play(tune, -1)'''

# initialize pygame clock
clock = pygame.time.Clock()

# Screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

# load game font
custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 50)
text = (custom_font.render("Space Invaders", True, (255,69,0)))

life_icon = pygame.image.load("../assets/sprites/player.png").convert()
life_icon.set_colorkey((0, 0, 0))

# initialize score and a custom font to display it
score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)
game_level = 0

# Main Loop
running = True
background = screen.copy()
#draw_background(background)

# spawn in player
player = Player(SCREEN_WIDTH / 2)

#screen.blit(background, (0, 0))
#draw_welcome(screen)
#pygame.display.flip()
#time.sleep(5)

while lives > 0 and running:

    # line up invaders in rows/cols when starting, or squad is wiped out
    if len(invaders) == 0:
        game_level += 1
        squad = Squad(INVADERS_ROWS, INVADERS_COLS, game_level, invader_bomb)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control player with arrow keys
        player.stop()  # always start from no motion state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # move player left if possible
                player.move_left()
            if event.key == pygame.K_RIGHT:  # move player right if possible
                player.move_right()
            if event.key == pygame.K_SPACE:
                fire_bullets(player.rect.midtop, player_fire)
        elif event.type == pygame.MOUSEBUTTONDOWN:	# keeping this for the mouse feature - moves player
            if pygame.mouse.get_pressed()[0]:
                player.x = pygame.mouse.get_pos()[0]

    screen.blit(background, (0,0))

    # update game objects
    lost = squad.march()
    if lost :	# if invaders reach player's row
        pygame.mixer.Sound.play(die_sound)
        lives -=1
        invaders.empty()	# clear the invaders to reinitialize level
        game_level -= 1		# and don't advance level
    player.update()
    bullets.update()
    bombs.update()

    for bullet in bullets:
        results = pygame.sprite.spritecollide(bullet, invaders, True)
        if results:	# shot an invader?
            pygame.mixer.Sound.play(hit_sound)
            score += results[0].rank * POINTS_PER_RANK	# increment score per rank hit
            invaders.remove(results[0])
            bullets.remove(bullet)

    results = pygame.sprite.spritecollide(player, bombs, True)
    if results:		# hit by invader bomb?
        pygame.mixer.Sound.play(die_sound)
        bombs.remove(results[0])
        lives -= 1
        invaders.empty()	# clear the invaders to reinitialize level
        game_level -= 1		# and don't advance level

    # draw game objects
    player.draw(screen)
    invaders.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet(screen)
    for bomb in bombs:
        bullet.draw_bomb(screen)


    #draw the score in the upper left corner
    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() -10, 0 ))

    # draw lives in the lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    # Update the display
    pygame.display.flip()

    # limit frame rate
    clock.tick(60)

#if won != "":
#    res_text = custom_font.render(won, True, (255, 69, 0))
#    screen.blit(res_text, ((SCREEN_WIDTH - text.get_width()) / 2, SCREEN_HEIGHT / 2))
#    pygame.display.flip()
#    time.sleep(5)

# Quit Pygame
pygame.quit()
sys.exit()
