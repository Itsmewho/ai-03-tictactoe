import random
import os
import time


class Board:
    def __init__(self):
        self.grid = [" "] * 9

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(" Intermediate AI (Blocker) ")
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]}")
        print("---|---|---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]}")
        print("---|---|---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]}")

    def available_moves(self):
        return [i for i, x in enumerate(self.grid) if x == " "]

    def check_win(self, player):
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


# ---- THE BRAIN


def get_smart_move(board):
    moves = board.available_moves()

    # Rule 1: Can AI win right now? (Offense)
    for move in moves:
        board.grid[move] = "X"  # Imagine making the move
        if board.check_win("X"):  # Did we win?
            board.grid[move] = " "  # Reset board
            return move  # Return the winning move
        board.grid[move] = " "  # Reset board

    # Rule 2: Will Human win next turn? (Defense)
    for move in moves:
        board.grid[move] = "O"  # Imagine Human moving there
        if board.check_win("O"):  # Would they win?
            board.grid[move] = " "  # Reset board
            return move  # BLOCK THEM!
        board.grid[move] = " "  # Reset board

    # Rule 3: Take Center (Best strategic spot)
    if 4 in moves:
        return 4

    return random.choice(moves)


# --- Game Loop ---
def play_game():
    board = Board()
    turn = "O"  # Human starts

    while True:
        board.display()

        if turn == "O":
            # Human Turn
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
            print("\nAI is calculating (Rules)...")
            time.sleep(0.5)
            move = get_smart_move(board)
            board.grid[move] = "X"

        # Check End Game
        if board.check_win(turn):
            board.display()
            print(f"\n{turn} Wins!")
            break
        if not board.available_moves():
            board.display()
            print("\nDraw!")
            break

        turn = "X" if turn == "O" else "O"


if __name__ == "__main__":
    play_game()
