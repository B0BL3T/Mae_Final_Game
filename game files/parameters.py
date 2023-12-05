#screen dimensions
TILE_SIZE = 64
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game play

# speeds are in pixels per frame and frame rate is 1/60 seconds

PLAYER_SPEED = 1

POINTS_PER_RANK = 10	# higher rank invaders are worth more
INVADERS_ROWS_PER_RANK = 2
INVADERS_ROWS = 6	# Rows (y) of invaders
INVADERS_COLS = 8	# Cols (x) of invaders
INVADERS_SPEED = 2	# initial invader speed (increases per level)
LEVEL_ACCEL = 2		# per-level acceleration
INVADERS_PITCH = 50	# spacing for rows and cols
INVADERS_DROP = 20	# y drop distance when squad hits horizontal bounds
TOP_ROW_Y = 50		# y position of top row

NUM_LIVES = 3

BULLET_SPEED = 10
BULLET_WIDTH =  3
BULLET_HEIGHT = 3
BULLET_COLOR = (0, 0, 255)
MAX_BULLETS = 2

PROBABILITY_BOMB = .05	# probability of each invader dropping a bomb (limited by MAX_BOMBS)
BOMB_SPEED = 10
BOMB_WIDTH =  3
BOMB_HEIGHT = 3
BOMB_COLOR = (0, 0, 255)
MAX_BOMBS = 4

TO_WIN = 10
SPACE_BLACK = (0, 0, 0)
