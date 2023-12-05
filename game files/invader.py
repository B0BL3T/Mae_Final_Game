import pygame
import random
from bomb import *
from parameters import *


class Invader(pygame.sprite.Sprite):

    def __init__(self, x, y, rank):
        super().__init__()

        self.rank = rank
        # use icon for rank of the invader
        self.image = pygame.image.load(f"../assets/sprites/enemy.png").convert()
        self.image = pygame.transform.flip(self.image, True, False)

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x, y)

    # march each invader in direction: 1=right, -1=left, 0=down
    # if any downward march reaches player's row, tell caller level is lost
    def update(self, direction):
        if direction != 0:
            self.x += invader_speed * 1
            self.rect.x = self.x
            # see if it will drop a bomb
            if random.random() < PROBABILITY_BOMB:
                drop_bomb(self.rect.midbottom, bomb_sound)
            return False
        else:
            self.y += INVADERS_DROP
            self.rect.y = self.y
            if self.y >= player.y:
                return True
            else:
                return False

    # check if an invader is out of horizontal roaming bound
    def reached_bound(self):
        if self.x < INVADERS_PITCH or self.x > SCREEN_WIDTH - self.rect.width - INVADERS_PITCH:
            return False
        else:
            return True

    def draw(self, screen):
        screen.blit(self.image, self.rect)


invaders = pygame.sprite.Group()

invader_speed = INVADERS_SPEED
invader_direction = 1

bomb_sound = 0


# setup a sqad of invaders at the initial position, direction, and speed for the level
def squad_init(num_rows, num_cols, game_level, invader_bomb):
    invader_speed = INVADERS_SPEED + LEVEL_ACCEL * (game_level - 1)
    invader_direction = 1
    #bomb_sound = invader_bomb

    # Line up invader_rows with increasing rank every INVADERS_ROWS_PER_RANK
    for row in range(num_rows):
        y = (num_rows - row) * INVADERS_PITCH + TOP_ROW_Y  # row numbers from bottom to top
        rank = row / INVADERS_ROWS_PER_RANK
        for x in range(num_cols):
            invaders.add(Invader((x + 1) * INVADERS_PITCH, y, rank))


def squad_march():
    # first march squad horizontally
    for invader in invaders:
        invader.update(1)
    for invader in invaders:
        if invader.reached_bound():
            # if any hit left/right bound, drop entire squad down a step.
            over_run = squad_down()  # if lowest reaches player level, return lost
            invader_direction *= -1
            break
    return over_run


def squad_down():
    over = False
    # march everone in squad down a step
    for invader in invaders:
        over = invader.update(0) or over  # look for ANY invader hit bottom row
    return over
