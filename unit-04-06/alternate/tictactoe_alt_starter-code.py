# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'

## Function name:
## Purpose:
## Input: 
## Output:
def make_board():
    pass

## Test statements
# print(make_board())
# quit()

## Function name:
## Purpose:
## Input: 
## Output:
def print_board(board):
    pass

## Test statements - Blank board
# print_board(make_board())
# quit()

## Test statements - Sample board
# test_board = [['X', '', 'O'],['O', 'X', 'X'],['X', '', 'O']]
# print_board(test_board)
# quit()

## Function name:
## Purpose:
## Input: 
## Output: 
def get_player_move(board):
    pass

## Test statements
# print(get_player_move(make_board()))
# quit()

## Function name:
## Purpose:
## Input:
## Output:
def get_computer_move(board):
    pass

## Test statements
# print(get_computer_move(make_board()))
# quit()    

win_conditions = [
    [
        [0, 0],
        [1, 1],
        [2, 2]
    ],
    # top row win condition
    [
        [0, 0],
        [0, 1],
        [0, 2]
    ],
    # middle row win condition
    [
        [1, 0],
        [1, 1],
        [1, 2]
    ],
    # there are 5 more win conditions to add here:
]

def check_for_winner(board):
    # test statement
    return 'keep playing'

# (Note: This `if` statement is important, please don't remove it.)
if __name__ == '__main__':
    print('Welcome to Tic-Tac-Toe!')

    # Ask the player what team they want to be.
    player_team = input('Do you want to be X or O?\n').upper()

    if player_team == 'X':
        computer_team = 'O'
    else:
        computer_team = 'X'

    # Get a fresh board.
    board = make_board()
    print_board(board)

    # Decide who goes first.
    whose_turn = random.choice([PLAYER, COMPUTER])

    print('The {} will go first.'.format(whose_turn))

    while True:
        # Figure out whose turn it is, and let them make a move.
        if whose_turn == PLAYER:
            row, col = get_player_move(board)
            board[row][col] = player_team

        else:
            row, col = get_computer_move(board)
            board[row][col] = computer_team
            print('The computer moved')

        print_board(board)

        # Check to see if someone won, and end the game if so.
        win_status = check_for_winner(board)
        if win_status != 'keep playing':
            if win_status == 'tie':
                print('-------------------')
                print("It's a tie!")
                break
            else:
                print('-------------------')
                print('The {} wins!'.format(whose_turn))
                break

        # If we've made it this far, nobody's won yet, so let's get ready for the next turn.
        if whose_turn == PLAYER:
            whose_turn = COMPUTER
        else:
            whose_turn = PLAYER
    print_board(board)
