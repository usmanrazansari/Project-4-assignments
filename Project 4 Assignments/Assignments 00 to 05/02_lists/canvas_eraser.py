import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)
CELL_SIZE = 20
ERASER_SIZE = 40
GRID_COLOR = (0, 0, 255)  # Blue
ERASER_COLOR = (255, 255, 255)  # White
BACKGROUND_COLOR = (200, 200, 200)  # Light gray

# Calculate grid dimensions
GRID_WIDTH = WINDOW_SIZE[0] // CELL_SIZE
GRID_HEIGHT = WINDOW_SIZE[1] // CELL_SIZE

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Canvas Eraser")

# Create the grid
grid = [[GRID_COLOR for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get mouse position and state
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()[0]  # Left mouse button
    
    # Calculate eraser position (centered on mouse)
    eraser_x = mouse_pos[0] - ERASER_SIZE // 2
    eraser_y = mouse_pos[1] - ERASER_SIZE // 2
    
    # If mouse is pressed, erase cells under the eraser
    if mouse_pressed:
        # Calculate which cells the eraser overlaps
        start_x = max(0, eraser_x // CELL_SIZE)
        end_x = min(GRID_WIDTH, (eraser_x + ERASER_SIZE) // CELL_SIZE + 1)
        start_y = max(0, eraser_y // CELL_SIZE)
        end_y = min(GRID_HEIGHT, (eraser_y + ERASER_SIZE) // CELL_SIZE + 1)
        
        # Set overlapping cells to white
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                grid[y][x] = ERASER_COLOR
    
    # Draw the grid
    screen.fill(BACKGROUND_COLOR)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, grid[y][x], rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)  # Grid lines
    
    # Draw the eraser
    eraser_rect = pygame.Rect(eraser_x, eraser_y, ERASER_SIZE, ERASER_SIZE)
    pygame.draw.rect(screen, (255, 0, 0), eraser_rect, 2)  # Red border for visibility
    
    pygame.display.flip()

pygame.quit()
sys.exit() 