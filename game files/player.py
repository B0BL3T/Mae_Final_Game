import pygame
import random
from parameters import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()

        self_image = pygame.image.load("../assets/sprites/player.png").convert()
        self_image.set_colorkey((0, 0, 0))

        self.image = self_image
        self.rect = self.image.get_rect()
        y = SCREEN_HEIGHT - self.rect.height
        # rect only stores integers, so we keep track of the position separately
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_velocity = 0
        self.y_velocity = 0

    def move_left(self):
        self.x_velocity = -1 * PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_velocity = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_velocity = 0

    def update(self):
        if self.rect.x > 0 and self.rect.x < SCREEN_WIDTH - player.rect.width:
            self.x += self.x_velocity
            self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
