Tic-Tac-Toe Game
A simple command-line implementation of the classic Tic-Tac-Toe game for two players. Players take turns choosing a position on a 3x3 grid to place their markers, either "X" or "O." The game checks for a winner or a tie after each turn.

Features

Two-player gameplay

Validates player input

Checks for wins and ties

Displays the game board after each turn

Game Instructions

The game is played on a 3x3 grid.

Players take turns to select a position by entering a number from 1 to 9, corresponding to the grid layout:

1 | 2 | 3

4 | 5 | 6

7 | 8 | 9

The first player to align three of their markers vertically, horizontally, or diagonally wins the game.

If all positions are filled without a winner, the game ends in a tie.

Code Structure

build_board(): Displays the current state of the game board.

player_turn(turn): Determines the current player's marker based on the turn number.

player_choice(player): Handles player input and updates the game state.

check_victory(): Checks if there's a winner or if the game is a tie.
