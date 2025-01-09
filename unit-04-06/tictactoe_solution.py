# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'

## Function name: make_board
## Purpose: Initialize a new, empty board
## Input: None
## Output: A new, empty board (list of lists)
def make_board():
    board = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append('')
        board.append(row)
    return board

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

def valid_move(board, row_number, col_number):
    return 1 <= row_number <= 3 and \
        1 <= col_number <= 3 and \
        board[row_number - 1][col_number - 1] == ''

## Function name: get_player_move
## Purpose: Asks for player move
## Input: current board (list of lists)
## Output: row and column number of selction
def get_player_move(board):
    while True:
        row_number = int(input('Input the row number where you would like to make your move (1-3): '))
        col_number = int(input('Input the column number where you would like to make your move (1-3): '))
        if not valid_move(board, row_number, col_number):
            print('Try again!')
        else:
            return row_number - 1, col_number - 1

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
                possible_moves.append([row, column])
    move = random.choice(possible_moves)
    return move

## Test statements
# print(get_computer_move(make_board()))
# quit()

win_conditions = [
    [[0, 0], [1, 1], [2, 2]],
    [[0, 0], [0, 1], [0, 2]],
    [[1, 0], [1, 1], [1, 2]],
    [[2, 0], [2, 1], [2, 2]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 1], [1, 1], [2, 1]],
    [[0, 2], [1, 2], [2, 2]],
    [[0, 2], [1, 1], [2, 0]],
]


## Function name: did_player_win_with_condition
## Purpose: given player, the current board, and the
##   win_condition, returns whether player won with that
##   win_condition
## Input: player (string)
## Input: current board (list of lists)
## Input: win_condition (list of lists)
## Output: True if player won with the given win_condition
def did_player_win_with_condition(player, board, win_condition):
    for (row, col) in win_condition:
        if board[row][col] != player:
            return False
    return True
## Test statements
# test_board = [['X', '', 'O'],['O', 'X', 'X'],['X', '', 'O']]
# print_board(test_board)
# print(did_player_win_with_condition('X', test_board, [[0, 0], [1, 1], [2, 2]]))
# quit()

def are_there_empty_spots(board):
    for row in board:
        for cell in row:
            if cell == '':
                return True
    return False

## Function name: get_game_status
## Purpose: Based on the board and winner, determine the game status
## Input: board (list of lists)
## Input: winner (string)
## Output: one of 'keep playing', 'tie', 'X', or 'O'
def get_game_status(board, winner):
    if winner is not None:
        return winner
    elif are_there_empty_spots(board):
        return 'keep playing'
    else:
        # all spots are filled but no winner is a tie
        return 'tie'

## Function name: check_for_winner
## Purpose: Checks if any of the win conditions have been met by either player
## Input: Current board (list of lists)
## Output: A string describing the win condition ("win", "tie", or "keep playing")
def check_for_winner(board):
    winner = None
    for win_condition in win_conditions:
        if did_player_win_with_condition('O', board, win_condition):
            winner = 'O'
        if did_player_win_with_condition('X', board, win_condition):
            winner = 'X'
    return get_game_status(board, winner)

## Test statements
# test_board = [['X', '', 'O'],['O', 'X', 'X'],['X', '', 'O']]
# print_board(test_board)
# print(check_for_winner(test_board))
# quit()

## Function name: is_game_over
## Purpose: Return whether the game is over based on the win_status
## Input: win_status (string)
## Output: True if the game is over, False if we need to keep playing
def is_game_over(win_status):
    if win_status == 'keep playing':
        return False
    if win_status == 'tie':
        return True
    if win_status == 'X':
        return True
    if win_status == 'O':
        return True

## Test statements
# print(is_game_over('keep playing'))
# print(is_game_over('tie'))
# quit()

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

        if is_game_over(win_status):
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
