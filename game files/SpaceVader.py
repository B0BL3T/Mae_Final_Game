import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cosmic Invaders")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

enemy_size = 50
enemy_x = width // 2 - enemy_size // 2
enemy_y = height // 4
enemy_speed = 3

bullet_size = 5
bullet_speed = 7
bullet_state = "ready"

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            '''elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_state = "fire"
                    bullet_x = player_x + player_size // 2
                    bullet_y = player_y'''

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        enemy_y += enemy_speed
        if enemy_y > height:
            enemy_y = 0

        if bullet_state == "fire":
            bullet_y -= bullet_speed
            pygame.draw.rect(screen, white, (bullet_x, bullet_y, bullet_size, bullet_size))

    # Update game logic here

    # Clear the screen
    screen.fill(black)

    # Draw game elements here
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    pygame.draw.rect(screen, white, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Update the display
    pygame.display.flip()