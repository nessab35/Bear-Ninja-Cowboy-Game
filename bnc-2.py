# cli-games/bnc.py
from random import randint


def open_message():
    '''Opening message'''
    print('''
          Get ready to play Bear, Ninja, Cowboy!
          ''') #telling player to get ready to play
    question_ = input("Would you like instructions? (yes/no)") # player is asked if they want instructions

    if question_ == "yes": # ifn player says 'yes' then instructions are printed
        print('''
              Bear, Ninja, Cowboy is an exciting game of strategy and skill! 
              Pit your wit against the computer! 
              Choose a player: Bear, Ninja, or Cowboy. 
              The computer chooses a player. 
              Everytime you win, you gain +1.
              If you lose, you lose -1
              Bear eats Ninja, Ninja defeats Cowboy, and Cowboy shoots Bear.
              ''')


def compare_choices(player, computer, player_score, rounds_):
    '''Compare player and computer'''
    if computer == player: # if player = computer there's a draw
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", player, "is shot by", computer)
            player_score -= 1 # if player loses, a point is taken away
        else: 
            print("You win!", player, "defeats", computer)
            player_score += 1 # if player wins, a point is gained
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
            player_score += 1
        else: 
            print("You lose!", player, "is eaten by", computer)
            player_score -= 1
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeated by", computer)
            player_score -= 1
        else: 
            print("You win!", player, "eats", computer)
            player_score += 1
    rounds_ += 1 # after each roud the total is counted for rounds
    return player_score, rounds_ # return player_score and rounds_


def play_again(player_score, rounds_):
    '''Play again'''
    response = input("Would you like to play again? (yes/no) > ") # asking if player wants to play again

    if response == "no": # if play again is no, score is printed out with how many rounds played
        print(f"Your final score: {player_score}/{rounds_}")
        return False # return false ends game
    elif response == "yes": # if answer is yes
        return True # game continues
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") # if any other response is enter, error message pops up
        return play_again(player_score, rounds_) # return funtion



roles = ["Bear", "Ninja", "Cowboy"] # assiging roles
player_score = 0 # assigning player score to 0
rounds_ = 0 # assigning rounds to 0
play_game = True # play_again assigned to true
first_run = True # first run assigned to true

# as long as play_again is true, game runs
while play_game:
    if first_run: # if it's first time playing
        open_message() # open message is showed
        first_run = False # then first run is returned false

    computer = roles[randint(0,2)] # assigned computer to random roles
    player_choice = input("Bear, Ninja, Cowboy?> ") # player is asked to choose role

    while player_choice not in roles: # if player not in roles, error message occurs
        print("Invalid choice. Please choose from Bear, Ninja, or Cowboy.")
        player_choice = input("Bear, Ninja, Cowboy?> ")

    # player_score, rounds_ is based off of the compare choices function
    player_score, rounds_ = compare_choices(player_choice, computer, player_score, rounds_)
    if not play_again(player_score, rounds_): # if player does not want play again, game ends
        break
