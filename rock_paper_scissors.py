#If player_A chooses rock and player_B chooses scissors, player A wins.
#If player_A chooses paper and player_B chooses rock, player A wins.
#If player_A chooses scissors and player_B chooses paper, player A wins.
#If both players choose the same item, neither player wins. It's a tie.

import random
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

def prompt(message):
    print(f'===> {message}')

def valid_input(user_choice):
    while user_choice not in VALID_CHOICES:
        prompt(f'Invalid game selection. Please input: {", ".join(VALID_CHOICES)}')
        user_choice = input()
    return user_choice

def winner_result(player_input, computer_input):
    prompt(f'You chose {player_input}, and computer chose {computer_input}')

    if player_input == 'rock' and computer_input == 'scissors':
        prompt('Player Wins!')
    elif player_input == 'paper' and computer_input == 'rock':
        prompt('Player Wins!')
    elif player_input == 'scissors' and computer_input == 'paper':
        prompt('Player Wins!')
    elif player_input == computer_input:
        prompt("It's a Tie")
    else:
        prompt('Computer Wins!')

while True:
    prompt("Welcome to rock paper scissors!")
    prompt("Please select either rock, paper, or scissors")
    player_input = input()

    player_input = valid_input(player_input)
    
    computer_selection = random.choice(VALID_CHOICES)

    winner_result(player_input, computer_selection)

    while True:
        prompt('Do you want to play again (y/n)?')
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
    
    if answer[0] == 'n':
        break