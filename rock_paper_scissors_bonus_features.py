#If player_A chooses rock and player_B chooses scissors, player A wins.
#If player_A chooses paper and player_B chooses rock, player A wins.
#If player_A chooses scissors and player_B chooses paper, player A wins.
#If player_A chooses lizard and player_B chooses paper, player A wins
#If player_A chooses lizard and player_B chooses spock, player A wins
#If player_A chooses spock and player_B chooses rock, Player A wins
#If player_A chooses spock and player_B chooses scissors, Player A wins
#If both players choose the same item, neither player wins. It's a tie.

import random
VALID_CHOICES = {
    'r': 'rock (r)',
    'p':'paper (p)',
    'sc':'scissors (sc)',
    'l':'lizard (l)',
    'sp':'spock (sp)'
    }

PLAYER_SCORE = 0
COMPUTER_SCORE = 0

def prompt(message):
    print(f'===> {message}')

def valid_input(user_choice):
    while user_choice not in VALID_CHOICES:
        prompt(
            f'Invalid game selection. Please input: '
            f' {", ".join(VALID_CHOICES.values())}'
        )
        user_choice = input()
    return user_choice

def score_tracker(p_input, c_input, p_score, c_score):

    winning_combinations = {
        'r': ['sc', 'l'],
        'p': ['r', 'sp'],
        'sc': ['p', 'l'],
        'l': ['sp', 'p'],
        'sp': ['r', 'sc']
    }

    if c_input in winning_combinations[p_input]:
        p_score += 1
    elif p_input in winning_combinations[c_input]:
        c_score += 1

    return p_score, c_score

def winner_result(p_input, c_input):
    prompt(f'You chose {VALID_CHOICES[p_input]}, '
           f'and computer chose {VALID_CHOICES[c_input]}'
        )

    if p_input == 'r' and c_input in ('sc','l'):
        prompt('Player Wins!')
    elif p_input == 'p' and c_input in ('r', 'sp'):
        prompt('Player Wins!')
    elif p_input == 'sc' and c_input in ('p','l'):
        prompt('Player Wins!')
    elif p_input == 'l' and c_input in ('p','sp'):
        prompt('Player Wins!')
    elif p_input == 'sp' and c_input in ('sc','r'):
        prompt('Player Wins!')
    elif p_input == c_input:
        prompt("It's a Tie")
    else:
        prompt('Computer Wins!')

prompt(f'Welcome to {", ".join(VALID_CHOICES.values())}!')

while (PLAYER_SCORE < 3 and COMPUTER_SCORE < 3):
    prompt(f'Please select either {", ".join(VALID_CHOICES.values())}')

    player_input = input()
    player_input = valid_input(player_input)
    computer_selection = random.choice(list(VALID_CHOICES.keys()))

    winner_result(player_input, computer_selection)
    PLAYER_SCORE, computer_score = score_tracker(
        player_input,
        computer_selection,
        PLAYER_SCORE,
        COMPUTER_SCORE)

    print(f'Player Score: {PLAYER_SCORE} | Computer Score: {COMPUTER_SCORE}')

if PLAYER_SCORE == 3:
    print(f'Player is the grand winner: {PLAYER_SCORE} vs {COMPUTER_SCORE}')
elif COMPUTER_SCORE == 3:
    print(f'Computer is the grand winner: {COMPUTER_SCORE} vs {PLAYER_SCORE}')