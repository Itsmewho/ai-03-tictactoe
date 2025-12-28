import random
import os
import time


class Board:
    def __init__(self):
        self.grid = [" "] * 9

    def display(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Beginner AI (Random moves)")
        print(f" {self.grid[0]} | {self.grid[1]} | {self.grid[2]}")
        print("---|---|---")
        print(f" {self.grid[3]} | {self.grid[4]} | {self.grid[5]}")
        print("---|---|---")
        print(f" {self.grid[6]} | {self.grid[7]} | {self.grid[8]}")

    def is_full(self):
        return " " not in self.grid

    def check_win(self, player):
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # Rows
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # Cols
            (0, 4, 8),
            (2, 4, 6),  # Diagonals
        ]
        for a, b, c in wins:
            if self.grid[a] == self.grid[b] == self.grid[c] == player:
                return True
        return False


def play_game():
    board = Board()
    current_player = "O"  # Human starts

    while True:
        board.display()

        if current_player == "O":
            while True:
                try:
                    move = int(input("\nYour Move (1-9): ")) - 1
                    if 0 <= move <= 8 and board.grid[move] == " ":
                        board.grid[move] = "O"
                        break
                    else:
                        print("Invalid move, try again.")
                except ValueError:
                    print("Please enter a number.")

        else:
            print(f"\nAI ({current_player}) is picking a random spot...")
            time.sleep(0.5)
            available = [i for i, x in enumerate(board.grid) if x == " "]
            if available:
                move = random.choice(available)
                board.grid[move] = "X"

        # Check Win
        if board.check_win(current_player):
            board.display()
            print(f"\n{current_player} Wins!")
            break

        # Check Draw
        if board.is_full():
            board.display()
            print("\nDraw!")
            break

        # Switch Turn
        current_player = "X" if current_player == "O" else "O"


if __name__ == "__main__":
    play_game()
