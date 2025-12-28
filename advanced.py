import os
import math


class Board:
    def __init__(self):
        self.grid = [" "] * 9

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(" Expert AI (Minimax) ")
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]}")
        print("---|---|---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]}")
        print("---|---|---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]}")

    def available_moves(self):
        return [i for i, x in enumerate(self.grid) if x == " "]

    def check_winner(self, player):
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for a, b, c in wins:
            if self.grid[a] == self.grid[b] == self.grid[c] == player:
                return True
        return False

    def is_full(self):
        return " " not in self.grid


def minimax(board, is_maximizing):
    """
    Returns the Score of the board:
    +1 = X Wins (AI)
    -1 = O Wins (Human)
     0 = Draw
    """
    # 1. Base Case: Check terminal states
    if board.check_winner("X"):
        return 1
    if board.check_winner("O"):
        return -1
    if board.is_full():
        return 0

    if is_maximizing:
        # AI's Turn (Maximize Score)
        best_score = -math.inf
        for move in board.available_moves():
            board.grid[move] = "X"
            score = minimax(board, False)  # Recurse as Human
            board.grid[move] = " "  # Undo
            best_score = max(score, best_score)
        return best_score
    else:
        # Human's Turn (Minimize Score)
        best_score = math.inf
        for move in board.available_moves():
            board.grid[move] = "O"
            score = minimax(board, True)  # Recurse as AI
            board.grid[move] = " "  # Undo
            best_score = min(score, best_score)
        return best_score


def get_best_move(board):
    # Optimization: If board is empty, take Center (Indices 4).
    # Minimax on an empty 3x3 board takes a noticeable 1-2 seconds in Python.
    if len(board.available_moves()) == 9:
        return 4

    best_score = -math.inf
    best_move = None

    for move in board.available_moves():
        # Make the move
        board.grid[move] = "X"

        # Calculate the score of this path using Minimax
        score = minimax(board, False)

        # Undo the move
        board.grid[move] = " "

        # If this path is better than what we found so far, keep it
        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# ---- Game Loop
def play_game():
    board = Board()
    turn = "O"  # Human starts

    while True:
        board.display()

        if turn == "O":
            while True:
                try:
                    move = int(input("\nYour move (1-9): ")) - 1
                    if move in board.available_moves():
                        board.grid[move] = "O"
                        break
                    print("Invalid move.")
                except ValueError:
                    pass
        else:
            print("\nAI is calculating (Minimax)...")
            move = get_best_move(board)
            board.grid[move] = "X"

        if board.check_winner(turn):
            board.display()
            print(f"\n{turn} Wins!")
            break
        if board.is_full():
            board.display()
            print("\nDraw!")
            break

        turn = "X" if turn == "O" else "O"


if __name__ == "__main__":
    play_game()
