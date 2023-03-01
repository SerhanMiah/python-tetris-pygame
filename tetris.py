import pygame
import random
pygame.init()

# Set up the game window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tetris Game')


# Game Board
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]


# Creating Shapes
shapes = {
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


class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = BOARD_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    # creating the moviement
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def rotate(self):
        self.shape = [[self.shape[y][x] for y in range(
            len(self.shape))] for x in range(len(self.shape[0])-1, -1, -1)]

    def draw(self, surface):
        pass