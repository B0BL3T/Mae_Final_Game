import pygame
import sys
import os
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


def draw_background(screen):
    screen.fill(SPACE_BLACK)


background = screen.copy()

# buttons
play_button = pygame.image.load("../assets/sprites/button.png").convert()
quit_button = pygame.image.load("../assets/sprites/button.png").convert()

new_size_play_button = pygame.transform.scale(play_button, (209.25, 94.5))
new_size_quit_button = pygame.transform.scale(quit_button, (209.25, 94.5))

play_button_rect = new_size_play_button.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60))
quit_button_rect = new_size_quit_button.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60))


def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))


def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0


def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button_rect.collidepoint(mouse_pos):
                        return
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        screen.blit(new_size_play_button, play_button_rect)
        screen.blit(new_size_quit_button, quit_button_rect)

        custom_font = pygame.font.Font("../assets/fonts/space_invaders.ttf", 80)
        text = custom_font.render("Space Invaders", True, (0, 255, 0))
        screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

        custom_font_2 = pygame.font.Font("../assets/fonts/space_invaders.ttf", 40)
        play_text = custom_font_2.render("Play", True, (0, 255, 0))
        quit_text = custom_font_2.render("Quit", True, (0, 255, 0))
        screen.blit(play_text, ((SCREEN_WIDTH / 2) - 40, SCREEN_HEIGHT / 2 - 60))
        screen.blit(quit_text, ((SCREEN_WIDTH / 2) - 40, SCREEN_HEIGHT / 2 + 60))
        high_score_text = custom_font_2.render(f"High Score: {str(load_high_score())}", True, (0, 255, 0))
        screen.blit(high_score_text, ((SCREEN_WIDTH / 2) - 200, SCREEN_HEIGHT / 2 + 140))


        pygame.display.flip()


main_menu()

screen.blit(background, (0, 0))
pygame.display.set_caption("Space Invaders")

# Load the sound effects
hit_sound = pygame.mixer.Sound("../assets/sounds/enemy_explosion.mp3")  # invader killed
die_sound = pygame.mixer.Sound("../assets/sounds/player_die.mp3")  # player died
player_fire = pygame.mixer.Sound("../assets/sounds/default_shot.mp3")  # player fires
invader_bomb = pygame.mixer.Sound("../assets/sounds/torp_explosion.mp3")  # invader fires
music = pygame.mixer.Sound("../assets/music/electronic_senses_absolom.mp3")

pygame.mixer.Sound.play(music, -1)

# initialize pygame clock
clock = pygame.time.Clock()

# Screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

# load game font
custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 50)
text = (custom_font.render("Space Invaders", True, (255, 69, 0)))
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

life_icon = pygame.image.load("../assets/sprites/player.png").convert()
isize = life_icon.get_size()
life_icon = pygame.transform.scale(life_icon, (isize[0] * .1, isize[1] * .1))
life_icon.set_colorkey((255, 255, 255))

# initialize score and a custom font to display it
score = 0
lives = NUM_LIVES
game_level = 0

# Main Loop
running = True
# draw_background(background)

# spawn in player
player = Player(SCREEN_WIDTH / 2)

# screen.blit(background, (0, 0))
# draw_welcome(screen)
# pygame.display.flip()
# time.sleep(5)

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
                fire_bullet(player.rect.midtop, player_fire)
        elif event.type == pygame.USEREVENT:
            player.power_down()  # powerup over
        elif event.type == pygame.MOUSEBUTTONDOWN:  # keeping for mouse feature - moves player
            if pygame.mouse.get_pressed()[0]:
                player.x = pygame.mouse.get_pos()[0]

    screen.blit(background, (0, 0))

    # update game objects
    lost = squad.march()
    if lost:  # if invaders reach player's row
        pygame.mixer.Sound.play(die_sound)
        running = False
    player.update()
    bullets.update()
    bombs.update()

    for bullet in bullets:
        results = pygame.sprite.spritecollide(bullet, invaders, True)
        if results:  # shot an invader?
            pygame.mixer.Sound.play(hit_sound)
            score += results[0].rank * POINTS_PER_RANK  # increment score per rank hit
            if not player.power:
                bullets.remove(bullet)

    results = pygame.sprite.spritecollide(player, bombs, True)
    if results:  # hit by invader bomb? power?
        if (results[0].btype == "POWER"):
            pygame.mixer.Sound.play(hit_sound)  # need a power sound
            player.power_up()  # starting powerup, and timer to end it
            pygame.time.wait(500)
            pygame.time.set_timer(pygame.event.Event(pygame.USEREVENT, {}), POWERUP_DURATION * 1000)
        else:
            pygame.mixer.Sound.play(die_sound)
            lives -= 1
            pygame.time.wait(500)

    # draw game objects
    player.draw(screen)
    invaders.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet(screen)
    for bomb in bombs:
        bomb.draw_bomb(screen)

    # draw the score in the upper left corner
    text = score_font.render(f"{score}", True, (255, 69, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    # draw lives in the lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i * TILE_SIZE, 0))

    # Update the display
    pygame.display.flip()

    # limit frame rate
    clock.tick(60)

if (score > load_high_score()):
    save_high_score(score)

# Quit Pygame
pygame.quit()
sys.exit()
