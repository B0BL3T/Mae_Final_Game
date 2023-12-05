import pygame
from math import *
from parameters import *

# Invader attack by dropping bombs
class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.x, self.y = pos

    def update(self, player):
        # Move the bomb down the screen
        self.y += BOMB_SPEED		# note negative
        if self.y >= SCREEN_HEIGHT:
            bombs.remove(self)
        # Update the rect position
        self.rect.x, self.rect.y = self.x, self.y

    def draw_bomb(self, screen):
        # Draw the bomb to the screen
        pygame.draw.rect(screen, BOMB_COLOR, self.rect)

bombs = pygame.sprite.Group()

def drop_bomb(pos, invader_bomb):
    if len(bombs) <= MAX_BOMBS:
        bombs.add(Bomb(pos))
        pygame.mixer.Sound.play(invader_bomb)
