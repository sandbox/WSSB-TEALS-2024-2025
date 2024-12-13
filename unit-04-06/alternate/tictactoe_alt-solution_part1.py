# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'

## Function name: make_board
## Purpose: Initialize a new, empty board
## Input: None
## Output: A new, empty board (list of lists)
def make_board():
    new_board = []
    for row in range(0, 3):
        new_board.append([])
        for column in range(0, 3):
            new_board[row].append('')
    return new_board

## Test statements
# print(make_board())
# quit()

## Function name: print_board
## Purpose: prints a formatted board based on a list
## Input: board (list of lists)
## Output: None (prints formatted board)
def print_board(board):
    for row in board:
        my_row = ''
        for column in row:
            if column == '':
                my_row += '|   '
            else:
                my_row += '| ' + column + ' '
        my_row += '|'
        print(my_row)

## Test statements - Blank board
# print_board(make_board())
# quit()

## Test statements - Sample board
# test_board = [['X', '', 'O'],['O', 'X', 'X'],['X', '', 'O']]
# print_board(test_board)
# quit()

## Function name: get_player_move
## Purpose: Asks for player move
## Input: current board (list of lists)
## Output: row and column number of selction
def get_player_move(board):
    player_move = True
    while player_move:
        player_row = int(input("Pick a row")) - 1
        player_column = int(input("Pick a column")) - 1
        if board[player_row][player_column] == '':
            return [player_row, player_column]
        else:
            print("Try again!")

## Test statements
# print(get_player_move(make_board()))
# quit()

## Function name: get_computer_move
## Purpose: Generates a computer move from list of available spaces
## Input: current board (list of lists)
## Output: row and column number of selction
def get_computer_move(board):
    possible_moves = []
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column] == '':
                possible_moves += [[row, column]]
    move = random.choice(possible_moves)
    return move

## Test statements
# print(get_computer_move(make_board()))
# quit()    

win_conditions = [
    [[0, 0], [1, 1], [2, 2]],
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]]
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
