import pygame
import random
from parameters import *
from bomb import *


class Invader(pygame.sprite.Sprite):

    def __init__(self, x, y, rank):
        super().__init__()

        self.rank = rank
        # use icon for rank of the invader
        self.image = pygame.image.load(f"../assets/sprites/enemy.png").convert()
        imgsize = self.image.get_size()
        newsize = (imgsize[0] * .08, imgsize[1] * .08)
        self.image = pygame.transform.scale(self.image, newsize)

        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x, y)

    # march each invader in speed_direction (=0 to drop down)
    # if any downward march reaches player's row, tell caller level is lost
    def update(self, speed_direction, invader_bomb):
        if speed_direction != 0:
            self.x += speed_direction
            self.rect.x = self.x
            # see if it will drop a bomb
            if random.random() < PROBABILITY_BOMB:
                drop_bomb(self.rect.midbottom, invader_bomb)
            return False
        else:
            if self.x < 0:
                self.x = 1
            elif self.x > SCREEN_WIDTH - self.rect.width:
                self.x = SCREEN_WIDTH - self.rect.width
            self.y += INVADERS_DROP
            self.rect.y = self.y
            if self.y >= SCREEN_HEIGHT - 50:  # should be Player's height off bottom
                return True
            else:
                return False

    # check if an invader is out of horizontal roaming bound
    def reached_bound(self):
        # if self.x < INVADERS_PITCH or self.x > SCREEN_WIDTH - self.rect.width - INVADERS_PITCH:
        if self.x < 0 or self.x > SCREEN_WIDTH - self.rect.width:
            return True
        else:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)


invaders = pygame.sprite.Group()
