import pygame
from parameters import *


class Player(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()
        # Prepare normal and powered-up icons
        self.image1 = pygame.image.load("../assets/sprites/player.png").convert()
        isize = self.image1.get_size()
        self.image1 = pygame.transform.scale(self.image1, (isize[0] * .1, isize[1] * .1))
        self.image1.set_colorkey((255, 255, 255))

        self.imageP = pygame.image.load("../assets/sprites/player_powered_up.png").convert()
        isize = self.imageP.get_size()
        self.imageP = pygame.transform.scale(self.imageP, (isize[0] * .1, isize[1] * .1))
        self.imageP.set_colorkey((255, 255, 255))

        self.image = self.image1
        self.power = False
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

    def move_right(self):
        self.x_velocity = PLAYER_SPEED

    def stop(self):
        self.x_velocity = 0

    def update(self):
        self.x += self.x_velocity
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.rect.width:
            self.x = SCREEN_WIDTH - self.rect.width
        self.rect.x = self.x

    def power_up(self):
        self.image = self.imageP
        self.power = True

    def power_down(self):
        self.image = self.image1
        self.power = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
