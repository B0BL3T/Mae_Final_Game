#screen dimensions
TILE_SIZE = 64
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game play

# speeds are in pixels per frame and frame rate is 1/60 seconds

PLAYER_SPEED = 1

INVADERS_ROWS_PER_RANK = 2
INVADERS_ROWS = 6
INVADERS_COLS = 8
INVADERS_SPEED = 2	# initial invader speed (increases per level)
LEVEL_ACCEL = 2		# per-level accel
INVADERS_PITCH = 50	# spacing for rows and cols
INVADERS_DROP = 20	# y advance distance when squad hits horizontal bounds
TOP_ROW_Y = 50		# y position of top row

NUM_LIVES = 3

BULLET_SPEED = 10
BULLET_WIDTH =  3
BULLET_HEIGHT = 3
BULLET_COLOR = (0, 0, 255)
MAX_BULLETS = 1

PROBABILITY_BOMB = .05	# probability of each invader dropping a bomb (subject to MAX limit)
BOMB_SPEED = 10
BOMB_WIDTH =  3
BOMB_HEIGHT = 3
BOMB_COLOR = (0, 0, 255)
MAX_BOMBS = 3

TO_WIN = 10
SPACE_BLACK = (0, 0, 0)
