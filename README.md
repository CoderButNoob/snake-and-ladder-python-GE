#Snakes and Ladders Game

##Description

This Python program simulates the classic Snakes and Ladders game. Players roll a dice and move accordingly, encountering ladders that boost them up or snakes that pull them down. The game continues until a player reaches position 100.

##Features

Single-player mode

Two-player mode

Random dice rolling

Random move selection (No Play, Snake, or Ladder)

Ensures players do not exceed position 100

##How to Run

Ensure you have Python installed (Python 3 recommended).

Copy the code into a Python script (e.g., snakes_ladders.py).

Run the script using:

python snakes_ladders.py

Follow the on-screen instructions to play.

##Functions

start_game(): Initializes player position.

dice_roll(): Simulates rolling a six-sided dice.

choose_move(): Randomly selects a move (No Play, Snake, Ladder).

play_game(): Runs the game in single-player mode.

play_turn(player_pos): Handles a player's turn, updating their position.

count_dice_rolls(): Counts dice rolls needed to win.

two_player_game(): Allows two players to play, alternating turns.

##Game Rules

Players roll the dice to advance.

Landing on a ladder moves the player up.

Landing on a snake moves the player down.

The first player to reach exactly position 100 wins.

##Example Output

Player 1's Turn:
Dice rolled: 4
Move: Ladder
Ladder! Player moves up to: 4

Player 2's Turn:
Dice rolled: 3
Move: Snake
Snake! Player moves down to: 0
...
Congratulations! Player 1 won the game!



