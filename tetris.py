import pygame
import random

pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris')

# Define colors RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

COLORS = {
    "I": CYAN,
    "O": YELLOW,
    "T": PURPLE,
    "S": GREEN,
    "Z": RED,
    "J": BLUE,
    "L": ORANGE
}

# Creating Shapes
SHAPES = {
    "I": [
        [1, 1, 1, 1]
    ],
    "0": [
        [1, 1],
        [1, 1]
    ],
    "T": [
        [0, 1, 0],
        [1, 1, 1]
    ],
    "S": [
        [0, 1, 1],
        [1, 1, 0]
    ],
    "Z": [
        [1, 1, 0],
        [0, 1, 1]
    ],
    "J": [
        [1, 1, 0],
        [1, 1, 1]
    ],
    "L": [
        [0, 0, 1],
        [1, 1, 1]
    ]
}

# Define block size and grid dimensions
BLOCK_SIZE = 30
GRID_WIDTH = WINDOW_WIDTH // BLOCK_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // BLOCK_SIZE

# Define the game board
board = [[GRAY for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]

# Define the game variables
fall_speed = 0.5
score = 0
level = 1

# Define the function to draw the game board


def draw_board():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            pygame.draw.rect(
                window, board[row][col], (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(window, BLACK, (col * BLOCK_SIZE,
                             row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# New block with random 
def new_block():
    block = random.choice(list(SHAPES.keys()))
    color = COLORS[block]
    shape = SHAPES[block]
    return shape, color
