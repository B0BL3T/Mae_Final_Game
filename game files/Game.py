import pygame
import sys
import random
import time
from math import atan2, pi
from parameters import *
from player import *

SPACE_BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Main Loop

running = True

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - player.rect.width)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(SPACE_BLACK)

        pygame.display.flip()