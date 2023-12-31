#screen dimensions
TILE_SIZE = 64
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game play

# speeds are in pixels per frame and frame rate is 1/60 seconds

PLAYER_SPEED = 3

POINTS_PER_RANK = 10	# higher rank invaders are worth more
INVADERS_ROWS_PER_RANK = 2
INVADERS_ROWS = 4	# Rows (y) of invaders
INVADERS_COLS = 10	# Cols (x) of invaders
INVADERS_SPEED = 1	# initial invader speed (increases per level)
LEVEL_ACCEL = 1		# per-level acceleration
INVADERS_PITCH = 50	# spacing for rows and cols
INVADERS_DROP = 10	# y drop distance when squad hits horizontal bounds
TOP_ROW_Y = 40		# y position of top row

NUM_LIVES = 3

BULLET_SPEED = 8
BULLET_WIDTH =  5
BULLET_HEIGHT = 15
BULLET_COLOR = (0, 255, 0)
MAX_BULLETS = 2

PROBABILITY_BOMB = .001	# probability of each invader dropping a bomb (limited by MAX_BOMBS)
PROBABILITY_POWER = .08	# probability that a bomb is a powerup
BOMB_SPEED = 3
BOMB_WIDTH =  10
BOMB_HEIGHT = 10
BOMB_COLOR = (255, 100, 0)
PBOMB_COLOR = (255, 0, 255)	# power-up bomb
MAX_BOMBS = 4

POWERUP_DURATION = 10	# power up lasts for n seconds

TO_WIN = 10
SPACE_BLACK = (0, 0, 0)
