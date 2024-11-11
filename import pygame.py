import pygame

# Constants for the game
GRID_SIZE = 50  # Cell size in pixels
COLS, ROWS = 12, 12  # Grid dimensions
WIDTH, HEIGHT = COLS * GRID_SIZE, ROWS * GRID_SIZE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def draw_grid(screen, player_pos, enemy_pos):
    screen.fill(WHITE)

    # Draw grid
    for x in range(COLS):
        for y in range(ROWS):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Draw player and enemy
    pygame.draw.rect(screen, GREEN, (player_pos[0] * GRID_SIZE, player_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (enemy_pos[0] * GRID_SIZE, enemy_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

def move_enemy_toward_player(enemy_pos, player_pos):
    # Calculate the direction based on the player's position
    if enemy_pos[0] < player_pos[0]:   # Enemy is to the left of the player
        enemy_pos[0] += 1
    elif enemy_pos[0] > player_pos[0]:  # Enemy is to the right of the player
        enemy_pos[0] -= 1
    elif enemy_pos[1] < player_pos[1]:  # Enemy is above the player
        enemy_pos[1] += 1
    elif enemy_pos[1] > player_pos[1]:  # Enemy is below the player
        enemy_pos[1] -= 1
    return enemy_pos

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Enemy AI with Conditional Movement")

    # Set the player's initial position
    player_pos = [5, 5]
    enemy_pos = [10, 10]
    
    # Flag to check if player moved
    player_moved = False

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Move player and set player_moved flag to True
                if event.key == pygame.K_LEFT and player_pos[0] > 0:
                    player_pos[0] -= 1
                    player_moved = True
                elif event.key == pygame.K_RIGHT and player_pos[0] < COLS - 1:
                    player_pos[0] += 1
                    player_moved = True
                elif event.key == pygame.K_UP and player_pos[1] > 0:
                    player_pos[1] -= 1
                    player_moved = True
                elif event.key == pygame.K_DOWN and player_pos[1] < ROWS - 1:
                    player_pos[1] += 1
                    player_moved = True

        # Move enemy only if the player has moved
        if player_moved:
            enemy_pos = move_enemy_toward_player(enemy_pos, player_pos)
            player_moved = False  # Reset the flag after enemy moves

        # Draw everything
        draw_grid(screen, player_pos, enemy_pos)

        clock.tick(10)  # Limit the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
