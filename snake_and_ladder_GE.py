import random 

def start_game():
    return 0

def dice_roll():
    return random.randint(1,6)

def choose_move():
    return random.choice(["No play","Snake","Ladder"])

def play_game():
    
    player_pos = start_game()

    while player_pos < 100:
        player_pos = play_turn(player_pos)
        print(f"Current Position: {player_pos}")

    print("\n Congratulations!  ")

def play_turn(player_pos):
    dice_value = dice_roll()
    move = choose_move()
    
    print(f"\nDice rolled: {dice_value}")
    print(f"Move: {move}")

    if move == "No play":
        print("No movement. Player stays at:", player_pos)
    elif move == "Ladder":
        new_position = player_pos + dice_value
        if new_position <= 100:  # Ensure position does not exceed 100
            player_pos = new_position
            print("Ladder! Player moves up to:", player_pos)
        else:
            print("Ladder ignored! Player must land exactly on 100.")
    else:  # Snake
        player_pos -= dice_value
        if player_pos < 0:
            player_pos = 0  # Restart if below 0
            print("Snake! Player goes below 0 and restarts from 0.")
        else:
            print("Snake! Player moves down to:", player_pos)

    return player_pos

def count_dice_rolls():
    roll_count = 0
    player_pos = start_game()
    
    while player_pos < 100:
        roll_count += 1
        player_pos = play_turn(player_pos)
        print(f"Current Position: {player_pos} (Rolls: {roll_count})")
    
    print(f"\nCongratulations! You won the game in {roll_count} rolls.")

def two_player_game():
    player1_pos = start_game()
    player2_pos = start_game()
    turn = 1
    
    while player1_pos < 100 and player2_pos < 100:
        if turn % 2 == 1:
            print("\nPlayer 1's Turn:")
            player1_pos = play_turn(player1_pos)
            if player1_pos >= 100:
                print("\nCongratulations! Player 1 won the game!")
                break
        else:
            print("\nPlayer 2's Turn:")
            player2_pos = play_turn(player2_pos)
            if player2_pos >= 100:
                print("\nCongratulations! Player 2 won the game!")
                break
        turn += 1

# Start the two-player game
two_player_game()