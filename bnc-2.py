# cli-games/bnc.py
from random import randint


def open_message():
    print('''
          Get ready to play Bear, Ninja, Cowboy!
          ''')
    question_ = input("Would you like instructions? (yes/no)")

    if question_ == "yes":
        print('''
              Bear, Ninja, Cowboy is an exciting game of strategy and skill! 
              Pit your wit against the computer! 
              Choose a player: Bear, Ninja, or Cowboy. 
              The computer chooses a player. 
              Everytime you win, you gain +1.
              If you lose, you lose -1
              Bear eats Ninja, Ninja defeats Cowboy, and Cowboy shoots Bear.
              ''')


def compare_choices(player, computer, player_score, total):
    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", player, "is shot by", computer)
            player_score -= 1
        else: # computer is cowboy, player is ninja
            print("You win!", player, "defeats", computer)
            player_score += 1
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
            player_score += 1
        else: # computer is bear, player is ninja
            print("You lose!", player, "is eaten by", computer)
            player_score -= 1
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeated by", computer)
            player_score -= 1
        else: # computer is ninja, player is bear
            print("You win!", player, "eats", computer)
            player_score += 1
    total += 1
    return player_score, total


def play_again(player_score, total):
    response = input("Would you like to play again? (yes/no) > ")

    if response == "no":
        print(f"Your final score: {player_score}/{total}")
        return False
    elif response == "yes":
        return True
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return play_again(player_score, total)  # Recursive call in case of invalid input



roles = ["Bear", "Ninja", "Cowboy"]
player_score = 0
total = 0
play_game = True
first_run = True

while play_game:
    if first_run:
        open_message()
        first_run = False

    computer = roles[randint(0,2)]
    player_choice = input("Bear, Ninja, Cowboy?> ")

    while player_choice not in roles:
        print("Invalid choice. Please choose from Bear, Ninja, or Cowboy.")
        player_choice = input("Bear, Ninja, Cowboy?> ")

    player_score, total = compare_choices(player_choice, computer, player_score, total)
    if not play_again(player_score, total):
        break
