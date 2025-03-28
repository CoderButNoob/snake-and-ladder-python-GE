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