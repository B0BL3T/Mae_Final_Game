import pygame
from parameters import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)
        self.x, self.y = pos

    def update(self):
        # Move the bullet up the screen
        self.y -= BULLET_SPEED		# note negative
        if self.y <= 0:
            bullets.remove(self)
        # Update the rect position
        self.rect.x, self.rect.y = self.x, self.y

    def draw_bullet(self, screen):
        # Draw the bullet to the screen
        pygame.draw.rect(screen, BULLET_COLOR, self.rect)

bullets = pygame.sprite.Group()

def fire_bullet(pos, player_fire):
    if len(bullets) < MAX_BULLETS:
        bullets.add(Bullet(pos))
#        pygame.mixer.Sound.play(player_fire)
