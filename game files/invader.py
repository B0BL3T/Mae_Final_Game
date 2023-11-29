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
        
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x,y)

    # march each invader in direction: 1=right, -1=left, 0=down
    # if any horizontal march is out of screen width range, tell the caller to march down a row
    # if any down march reaches player level, tell caller game over
    def update(self, direction):
        if direction != 0:
            self.x += invader_speed * invader_direction
            self.rect.x = self.x
            if self.x < self.rect.width or self.x > SCREEN_WIDTH - 2*self.rect.width:
                return 1
            else:
                return 0
        else:
            self.y += INVADER_PITCH
            self.rect.y = self.y
            if self.y >= player.y:
                return 1
            else:
                return 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

invaders = pygame.sprite.Group()

invader_speed = INVADER_SPEED
invader_direction = 1

def init_squad(num_rows, num_cols, game_level):
    invader_speed = INVADER_SPEED + LEVEL_ACCEL * (game_level-1)
    invader_direction = 1

    # Line up invader_rows with increasing rank every INVADERS_ROWS_PER_RANK
    for row in range(num_rows):
        y = (num_rows - row) * SQUAD_PITCH + TOP_ROW_Y	# row numbers from bottom to top
        rank = row / INVADERS_ROWS_PER_RANK
        for x in range(SQUAD_PITCH, SCREEN_HEIGHT, SQUAD_PITCH):
            invaders.add(Invader(x, y, rank))

# march squad horizontally. if hit x-bounds, drop a row. if hit last row, return >0
def march_squad(a):
    outside = 0		# used to record if any hit x-bounds
    for invader in invaders:
        outside += invader.update(invader_direction)
    if outside > 0:	# now drop a row
        outside = 0	# used to record if any hit bottom row
        for invader in invaders:
            outside += invader.update(0)
        return outside
    else:
        return 0
