import pygame
from parameters import *
from invader import *

class Squad():
    # setup a squad of invaders at the initial position, direction, and speed for the level
    def __init__(self, num_rows, num_cols, game_level, bomb):
        self.direction = 1
        self.speed = INVADERS_SPEED + LEVEL_ACCEL * (game_level - 1)
        self.bomb_sound = bomb

        # Line up num_rows with increasing rank every INVADERS_ROWS_PER_RANK
        for row in range(num_rows):
            y = (num_rows - row) * INVADERS_PITCH + TOP_ROW_Y	# row numbers from bottom to top
            rank = (row // INVADERS_ROWS_PER_RANK) + 1
            for x in range(num_cols):
                invaders.add(Invader((x+1) * INVADERS_PITCH, y, rank))

    def march(self):
        # first march squad horizontally
        for invader in invaders:
            invader.update(self.direction * self.speed, self.bomb_sound)
            for invader in invaders:
                if invader.reached_bound():
# if any hit left/right bound, reverse direction and drop entire squad down a step.
                    self.direction *= -1
                    return self.march_down()	# if lowest reaches player level, return lost

    def march_down(self):
        over = False
        # march everyone in squad down a step
        for invader in invaders:
            over = invader.update(0, self.bomb_sound) or over  # ANY invader on bottom row?
        return over
