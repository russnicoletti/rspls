import random
import sys

ROCK_NUMBER = 0
SPOCK_NUMBER = 1
PAPER_NUMBER = 2
LIZARD_NUMBER = 3
SCISSORS_NUMBER = 4
NAME_TO_NUMBER_DICT = {'rock': ROCK_NUMBER, 'Spock': SPOCK_NUMBER, 'paper': PAPER_NUMBER, 'lizard': LIZARD_NUMBER, 'scissors': SCISSORS_NUMBER}
NUMBER_TO_NAME_DICT = {ROCK_NUMBER: 'rock', SPOCK_NUMBER: 'Spock', PAPER_NUMBER: 'paper', LIZARD_NUMBER: 'lizard', SCISSORS_NUMBER: 'scissors'}

# -- Resolution matrix --
# The player choice determines the row.
# The computer choice determines the column.
# row/column 0: rock
# row/column 1: Spock
# row/column 2: paper
# row/column 3: lizard
# row/column 4: scissors
PLAYER_WINS = 0
COMPUTER_WINS = 1
TIE = 2
RESOLUTION_OUTCOME_MATRIX = \
    [ \
     [TIE, COMPUTER_WINS, COMPUTER_WINS, PLAYER_WINS, PLAYER_WINS], \
     [PLAYER_WINS, TIE, COMPUTER_WINS, COMPUTER_WINS, PLAYER_WINS], \
     [PLAYER_WINS, PLAYER_WINS, TIE, COMPUTER_WINS, COMPUTER_WINS], \
     [COMPUTER_WINS, PLAYER_WINS, PLAYER_WINS, TIE, COMPUTER_WINS], \
     [COMPUTER_WINS, COMPUTER_WINS, PLAYER_WINS, PLAYER_WINS, TIE] \
    ]

# Resolution descriptions
ROCK_ROCK = 'rock-rock'
ROCK_SPOCK = 'Spock vaporizes rock'
ROCK_PAPER = 'paper covers rock'
ROCK_LIZARD = 'rock crushes lizard'
ROCK_SCISSORS = 'rock crushes scissors'
SPOCK_ROCK = ROCK_SPOCK
SPOCK_SPOCK = 'Spock-Spock'
SPOCK_PAPER = 'paper disproves Spock'
SPOCK_LIZARD = 'lizard poisons Spock'
SPOCK_SCISSORS = 'Spock smashes scissors'
PAPER_ROCK = ROCK_PAPER
PAPER_SPOCK = SPOCK_PAPER
PAPER_PAPER = 'paper-paper'
PAPER_LIZARD = 'lizard eats paper'
PAPER_SCISSORS = 'scissors cuts paper'
LIZARD_ROCK = ROCK_LIZARD
LIZARD_SPOCK = SPOCK_LIZARD
LIZARD_PAPER = PAPER_LIZARD
LIZARD_LIZARD = 'lizard-lizard'
LIZARD_SCISSORS = 'scissors decapitates lizard'
SCISSORS_ROCK = ROCK_SCISSORS
SCISSORS_SPOCK = SPOCK_SCISSORS
SCISSORS_PAPER = PAPER_SCISSORS
SCISSORS_LIZARD = LIZARD_SCISSORS
SCISSORS_SCISSORS = 'scissors-scissors'

RESOLUTION_DESCRIPTION_MATRIX = \
    [ \
     [ ROCK_ROCK, ROCK_SPOCK, ROCK_PAPER, ROCK_LIZARD, ROCK_SCISSORS], \
     [ SPOCK_ROCK, SPOCK_SPOCK, SPOCK_PAPER, SPOCK_LIZARD, SPOCK_SCISSORS], \
     [ PAPER_ROCK, PAPER_SPOCK, PAPER_PAPER, PAPER_LIZARD, PAPER_SCISSORS], \
     [ LIZARD_ROCK, LIZARD_SPOCK, LIZARD_PAPER, LIZARD_LIZARD, LIZARD_SCISSORS], \
     [ SCISSORS_ROCK, SCISSORS_SPOCK, SCISSORS_PAPER, SCISSORS_LIZARD, SCISSORS_SCISSORS] \
    ]

def name_to_number(name):
    if not name in NAME_TO_NUMBER_DICT:
        return -1

    return NAME_TO_NUMBER_DICT[name]

def number_to_name(name):
    if not name in NUMBER_TO_NAME_DICT:
        return -1

    return NUMBER_TO_NAME_DICT[name]

def rspls(player_choice):
    print('')

    player_choice_number = name_to_number(player_choice)
    computer_choice_number = random.randrange(0, 5)
    print('players choice is', player_choice)
    print('computer choice is', number_to_name(computer_choice_number))

    resolution_outcome = RESOLUTION_OUTCOME_MATRIX[player_choice_number][computer_choice_number]
    resolution_description = RESOLUTION_DESCRIPTION_MATRIX[player_choice_number][computer_choice_number]
    winner_description = ''
    if resolution_outcome == PLAYER_WINS:
        winner_description = 'player wins!'
    elif resolution_outcome == COMPUTER_WINS:
        winner_description = 'computer wins!'
    else:
        winner_description = 'tie!'

    print(resolution_description + ', '+ winner_description)

if len(sys.argv) == 2:
    if  sys.argv[1] == 'test':

        print('rock is 0:\t', name_to_number('rock') == 0)
        print('Spock is 1:\t', name_to_number('Spock') == 1)
        print('paper is 2:\t', name_to_number('paper') == 2)
        print('lizard is 3:\t', name_to_number('lizard') == 3)
        print('scissors is 4:\t', name_to_number('scissors') == 4)

        print('0 is rock:\t', number_to_name(0) == 'rock')
        print('1 is lizard:\t', number_to_name(1) == 'Spock')
        print('2 is paper:\t', number_to_name(2) == 'paper')
        print('3 is lizard:\t', number_to_name(3) == 'lizard')
        print('4 is scissors:\t', number_to_name(4) == 'scissors')

        print('rock-rock, tie:\t\t\t' + str(RESOLUTION_OUTCOME_MATRIX[ROCK_NUMBER][ROCK_NUMBER] == TIE))
        print('rock-Spock, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[ROCK_NUMBER][SPOCK_NUMBER] == COMPUTER_WINS))
        print('rock-paper, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[ROCK_NUMBER][PAPER_NUMBER] == COMPUTER_WINS))
        print('rock-lizard, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[ROCK_NUMBER][LIZARD_NUMBER] == PLAYER_WINS))
        print('rock-scissors, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[ROCK_NUMBER][SCISSORS_NUMBER] == PLAYER_WINS))
        print('Spock-rock, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SPOCK_NUMBER][ROCK_NUMBER] == PLAYER_WINS))
        print('Spock-Spock, tie:\t\t' + str(RESOLUTION_OUTCOME_MATRIX[SPOCK_NUMBER][SPOCK_NUMBER] == TIE))
        print('Spock-paper, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SPOCK_NUMBER][PAPER_NUMBER] == COMPUTER_WINS))
        print('Spock-lizard, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SPOCK_NUMBER][LIZARD_NUMBER] == COMPUTER_WINS))
        print('Spock-scissors, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SPOCK_NUMBER][SCISSORS_NUMBER] == PLAYER_WINS))
        print('paper-rock, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[PAPER_NUMBER][ROCK_NUMBER] == PLAYER_WINS))
        print('paper-Spock, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[PAPER_NUMBER][SPOCK_NUMBER] == PLAYER_WINS))
        print('paper-paper, tie:\t\t' + str(RESOLUTION_OUTCOME_MATRIX[PAPER_NUMBER][PAPER_NUMBER] == TIE))
        print('paper-lizard, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[PAPER_NUMBER][LIZARD_NUMBER] == COMPUTER_WINS))
        print('paper-scissors, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[PAPER_NUMBER][SCISSORS_NUMBER] == COMPUTER_WINS))
        print('lizard-rock, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[LIZARD_NUMBER][ROCK_NUMBER] == COMPUTER_WINS))
        print('lizard-Spock, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[LIZARD_NUMBER][SPOCK_NUMBER] == PLAYER_WINS))
        print('lizard-paper, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[LIZARD_NUMBER][PAPER_NUMBER] == PLAYER_WINS))
        print('lizard-lizard, tie:\t\t' + str(RESOLUTION_OUTCOME_MATRIX[LIZARD_NUMBER][LIZARD_NUMBER] == TIE))
        print('lizard-scissors, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[LIZARD_NUMBER][SCISSORS_NUMBER] == COMPUTER_WINS))
        print('scissors-rock, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SCISSORS_NUMBER][ROCK_NUMBER] == COMPUTER_WINS))
        print('scissors-Spock, computer wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SCISSORS_NUMBER][SPOCK_NUMBER] == COMPUTER_WINS))
        print('scissors-paper, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SCISSORS_NUMBER][PAPER_NUMBER] == PLAYER_WINS))
        print('scissors-lizard, player wins:\t' + str(RESOLUTION_OUTCOME_MATRIX[SCISSORS_NUMBER][LIZARD_NUMBER] == PLAYER_WINS))
        print('scissors-scissors, tie:\t\t' + str(RESOLUTION_OUTCOME_MATRIX[SCISSORS_NUMBER][SCISSORS_NUMBER] == TIE))
    else:
        print('Invalid argument')
        sys.exit()
else:

    PLAYER_CHOICE_DICT = {'r': 'rock', 'S': 'Spock', 'p': 'paper', 'l': 'lizard', 's': 'scissors'}
    prompt = '\n(r)ock, (S)pock, (p)aper, (l)izard, (s)cissors, (e)xit: '
    player_choice_input = input(prompt)

    while player_choice_input != 'e':
        if player_choice_input in PLAYER_CHOICE_DICT:
            player_choice = PLAYER_CHOICE_DICT[player_choice_input]
            rspls(player_choice)
        player_choice_input = input(prompt)
