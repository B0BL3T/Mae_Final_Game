import pygame
from parameters import *

class Player(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()

        self.image = pygame.image.load("../assets/sprites/player.png").convert()
        imgsize = self.image.get_size()
        newsize = (imgsize[0] * .1, imgsize[1] * .1)
        self.image = pygame.transform.scale(self.image, newsize)
        self.image.set_colorkey((,255 255, 255))
        self.rect = self.image.get_rect()
        y = SCREEN_HEIGHT - self.rect.height
        # rect only stores integers, so we keep track of the position separately
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_velocity = 0
        self.y_velocity = 0

    def move_left(self):
        if self.rect.x > 0:
            self.x_velocity = -1 * PLAYER_SPEED

    def move_right(self):
        if self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.x_velocity = PLAYER_SPEED

    def stop(self):
        self.x_velocity = 0

    def update(self):
        self.x += self.x_velocity
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect)
