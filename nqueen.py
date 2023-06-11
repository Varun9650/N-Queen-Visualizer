import pygame
from pygame.locals import *

# Constants for the chessboard
CELL_SIZE = 60
QUEEN_COLOR = (255, 0, 0)
EMPTY_COLOR = (255, 255, 255)

# Initialize pygame
pygame.init()

# Function to draw the chessboard
def draw_board(board, screen):
    for row in range(len(board)):
        for col in range(len(board[row])):
            color = QUEEN_COLOR if board[row][col] == 1 else EMPTY_COLOR
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Function to validate queen placement
def is_safe(board, row, col):
    # Check row and column
    for i in range(len(board)):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check diagonals
    for i in range(len(board)):
        for j in range(len(board)):
            if (i + j == row + col) or (i - j == row - col):
                if board[i][j] == 1:
                    return False

    return True

# Backtracking algorithm to solve N-Queens
def solve_n_queens(board, col, screen):
    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            draw_board(board, screen)
            pygame.time.wait(200)  # Add delay for visualization

            if solve_n_queens(board, col + 1, screen):
                return True

            board[row][col] = 0
            draw_board(board, screen)
            pygame.time.wait(200)  # Add delay for visualization

    return False

# Main function
def main():
    running = True

    # User input for N
    n = int(input("Enter the value of N: "))

    # Create the chessboard
    board = [[0] * n for _ in range(n)]
    screen = pygame.display.set_mode((n * CELL_SIZE, n * CELL_SIZE))

    solve_n_queens(board, 0, screen)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    main()
