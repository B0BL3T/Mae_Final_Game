import pygame
import random
from parameters import *


class Invader(pygame.sprite.Sprite):

    def __init__(self, x, y, rank):
        super().__init__()

        self.rank = rank
        # use icon for rank of the invader
        self.image = pygame.image.load(f"../assets/sprites/invader{rank}.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x, y)

    # march each invader in direction: 1=right, -1=left, 0=down
    # if any down march reaches player level, tell caller game over
    def update(self, direction):
        if direction != 0:
            self.x += invader_speed * invader_direction
            self.rect.x = self.x
            return 0
        else:
            self.y += INVADER_DROP
            self.rect.y = self.y
            if self.y >= player.y:
                return 1
            else:
                return 0

    # check if an invader is out of horizontal roaming bound
    def reached_bound(self):
        if self.x < MARCH_XBOUNDARY or self.x > SCREEN_WIDTH - self.rect.width - MARCH_XBOUNDARY:
            return False
        else:
            return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)


invaders = pygame.sprite.Group()

invader_speed = INVADERS_SPEED
invader_direction = 1


# setup a sqad of invaders at the initial position, direction, and speed for the level
def init_squad(num_rows, num_cols, game_level):
    invader_speed = INVADERS_SPEED + LEVEL_ACCEL * (game_level - 1)
    invader_direction = 1

    # Line up invader_rows with increasing rank every INVADERS_ROWS_PER_RANK
    for row in range(num_rows):
        y = (num_rows - row) * INVADERS_PITCH + TOP_ROW_Y  # row numbers from bottom to top
        rank = row / INVADERS_ROWS_PER_RANK
        for x in range(INVADERS_PITCH, SCREEN_HEIGHT, INVADERS_PITCH):
            invaders.add(Invader(x, y, rank))


def march_squad():
    # first march squad horizontally
    for invader in invaders:
        invader.update(invader_direction)
    for invader in invaders:
        # check if any hit bounds, drop the squad down a step. if hit player level, return 0
        if invader.reached_bound():
            game_over = march_down()
            invader_direction *= -1
            break
    return game_over


def march_down():
    gameover = 0
    for invader in invaders:
        gameover += invader.update(0)
    return gameover
