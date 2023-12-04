import pygame
import sys
import random
import time
from math import atan2, pi
from player import Player
from parameters import *
from utilities import draw_background, add_fish, add_enemies, add_bullets
from bullet import bullets

# import the class Fish and fishes container from the module fish
from invader import Invader, invaders

# Initialize Pygame
pygame.init()

# play background music
pygame.mixer.Sound.play(tune, -1)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load the sound effects
'''kill_sound = pygame.mixer.Sound("../Assets/Sounds/enemy_explosion.mp3")  # invader killed
die_sound = pygame.mixer.Sound("../assets/sounds/player_die.mp3")    # player died
# bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav") #what does this do??
bang = pygame.mixer.Sound('../assets/sounds/boom.wav')
tune = pygame.mixer.Sound("../assets/sounds/we_have_time.ogg")
torpedo_shot = pygame.mixer.Sound("../Assets/Sounds/torpedo_shot.wav")

# initialize pygame clock
clock = pygame.time.Clock()

# Screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

# load game font
custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 50)
text = (custom_font.render("Chomp", True, (255,69,0)))

life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0, 0, 0))

# initialize score and a custom font to display it
score = 0
lives = NUM_LIVES
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)
game_level = 1

background = screen.copy()
draw_background(background)'''

# Main Loop
running = True
background = screen.copy()
draw_background(background)

# spawn in player
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - player.rect.width)

# line up invaders in rows/cols
init_squad(INVADERS_ROWS, INVADERS_COLS)

screen.blit(background, (0, 0))
draw_welcome(screen)
pygame.display.flip()
time.sleep(5)

while lives > 0 and running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control player with arrow keys
        player.stop()  # always start from no motion state
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player.rect.y > 0:  # move player up if event key is up AND POSSIBLE
                player.move_up()
            if event.key == pygame.K_DOWN and player.rect.y < SCREEN_HEIGHT - player.rect.height:  # move player down if event key is down AND POSSIBLE
                player.move_down()
            if event.key == pygame.K_LEFT and player.rect.x > 0:  # move player left if event key is left AND POSSIBLE
                player.move_left()
            if event.key == pygame.K_RIGHT and player.rect.x < SCREEN_WIDTH - player.rect.width:  # move player right if event key is right AND POSSIBLE
                player.move_right()
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(bang)
                pos = player.rect.midright
                add_bullets(1, pos, angle)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() [0]:
                    player.x, player.y = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = player.rect.midright
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = - atan2(mouse_y - pos[1], mouse_x - pos[0])
                add_bullets(1, pos, angle)


    for bullet in bullets:

        if bullet.rect.x > SCREEN_WIDTH:
            bullets.remove(bullet)

        for enemy in enemies:
            bullet_enemy = pygame.sprite.spritecollide(bullet, enemies, True)
            if bullet_enemy: #enemy is killed?
                pygame.mixer.Sound.play(bang)
                score += len(bullet_enemy) # increment score is you shoot an enemy
                enemies.remove(enemy)
                add_enemies(1)
                bullets.remove(bullet)
                pos = player.rect.midright
                add_bullets(1, pos, angle)

        for fish in fishes:
            bullet_fish = pygame.sprite.spritecollide(bullet, fishes, True)
            if bullet_fish:
                score -= len(bullet_fish) #decrease score if you shoot a friend
                fishes.remove(fish)
                add_fish(1)


    screen.blit(background, (0,0))

    # update game objects
    fishes.update()
    player.update()
    bullets.update(player)

    for enemy in enemies:
        direction = atan2(player.y - enemy.y, player.x - enemy.x)
        enemy.update(direction)

    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        score += len(result)
        # play chomp sound
        pygame.mixer.Sound.play(chomp)
        #add new fish
        add_fish(len(result))

    # check for collisions between player and enemy fish
    # remove fish if there is a collision and reduce the
    # number of lives
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        lives -= len(result)
        #play chomp sound
        pygame.mixer.Sound.play(hurt)
        # add new fish
        add_enemies(len(result))

    # if any fish have moved off the left side of the screen, remove them
    # and add a new fish off the right side of the screen

    for fish in fishes:
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(SCREEN_WIDTH + TILE_SIZE * 2,
                    random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

    # if any enemies have moved off the left side of the screen, remove them
    # and add a new enemy off the right side of the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:
            enemies.remove(enemy)
            add_enemies(1)

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet(screen)

    #draw the score in the upper left corner
    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() -10, 0 ))

    # draw lives in the lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    # draw out bullets
    for bullet in bullets:
        bullet.draw_bullet(screen)

    # Update the display
    pygame.display.flip()

    # limit frame rate
    clock.tick(60)
    if pygame.time.get_ticks() > 60000:  # 1 min
        if score >= TO_WIN:
            won = "You Won!"
        else:
            won = "You Lost!"
        running = False

if won != "":
    res_text = custom_font.render(won, True, (255, 69, 0))
    screen.blit(res_text, ((SCREEN_WIDTH - text.get_width()) / 2, SCREEN_HEIGHT / 2))
    pygame.display.flip()
    time.sleep(5)

# Quit Pygame
pygame.quit()
sys.exit()
