# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'


# Here are the empty functions that it's your job to implement!
# Check the assignment carefully to see what each function is supposed to do.
# Don't rename these functions! You can absolutely write extra functions aside from these
# ones if you want, but don't change the names of the five functions please.

# Plan: What is make board supposed to output?
def make_board():
    board = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            row.append('')
        board.append(row)
    return board

assert make_board() == [['', '', ''], ['', '', ''], ['', '', '']]

def print_board(board):
    for row in board:
        row_str = '| '
        for cell in row:
            if cell == '':
                row_str += ' '
            else:
                row_str += cell
            row_str += ' | '
        print(row_str)

# We're expecting the following code to output
print('Printing an empty board')
print_board(make_board())

print('Printing an example board')
print_board([
  ['X', '', 'O'],
  ['O', 'X', 'X'],
  ['X', '', 'O']
])

def valid_move(board, row_number, col_number):
    return row_number is not None and 1 <= row_number <= 3 and col_number is not None and 1 <= col_number <= 3 and board[row_number - 1][col_number - 1] == ''

def get_player_move(board):
    while True:
        row_number = int(input('Input the row number where you would like to make your move (1-3): '))
        col_number = int(input('Input the column number where you would like to make your move (1-3): '))
        if not valid_move(board, row_number, col_number):
            print('Please input a valid move!')
        else:
            break
    return row_number - 1, col_number - 1
print('Try running get_player_move with the input of row number 3 and col number 2')
assert get_player_move(make_board()) == (2, 1)

# What is the expectation for get_computer_move?
# returning the first spot open for the computer
def get_computer_move(board):
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] == '':
                return row, col

assert get_computer_move([
  ['X', '', 'O'],
  ['O', 'X', 'X'],
  ['X', '', 'O']
]) == (0, 1)
assert get_computer_move([
  ['X', 'O', 'X'],
  ['O', 'X', 'X'],
  ['O', '', '']
]) == (2, 1)

def get_win_conditions():
    return [
        [[0, 0], [1, 1], [2, 2]],
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 2], [1, 1], [2, 0]],
    ]
assert len(get_win_conditions()) == 8

def did_turn_win(whose_turn, board, win_condition):
    for (row, col) in win_condition:
        if board[row][col] != whose_turn:
            return False
    return True

assert did_turn_win('X', [['X', 'X', 'X'], ['O', '', 'O'], ['', 'O', '']], [[0, 0], [0, 1], [0, 2]])
assert not did_turn_win('O', [['X', 'X', 'X'], ['O', '', 'O'], ['', 'O', '']], [[0, 0], [0, 1], [0, 2]])
assert did_turn_win('O', [['O', 'O', 'O'], ['X', '', 'X'], ['', 'X', '']], [[0, 0], [0, 1], [0, 2]])

def are_there_empty_spots(board):
    for row in board:
        for cell in row:
            if cell == '':
                return True
    return False

def get_game_status(board, winner):
    if winner is not None:
        return winner
    elif are_there_empty_spots(board):
        return 'keep playing'
    else:
        # all spots are filled but no winner is a tie
        return 'tie'
assert get_game_status(make_board(), None) == 'keep playing'
assert get_game_status(make_board(), 'X') == 'X'
assert get_game_status(make_board(), 'O') == 'O'
assert get_game_status([
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', 'X']
], None) == 'tie'

def check_for_winner(board):
    win_conditions = get_win_conditions()
    winner = None
    for win_condition in win_conditions:
        if did_turn_win('O', board, win_condition):
            winner = 'O'
        if did_turn_win('X', board, win_condition):
            winner = 'X'
    return get_game_status(board, winner)
assert check_for_winner(make_board()) == 'keep playing'
assert check_for_winner([
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'X']
]) == 'X'
assert check_for_winner([
    ['X', 'O', 'X'],
    ['O', 'O', 'O'],
    ['O', 'X', 'X']
]) == 'O'
assert check_for_winner([
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', 'X']
]) == 'tie'

def is_game_over(win_status):
    if win_status == 'keep playing':
        return False
    if win_status == 'tie':
        return True
    if win_status == 'X':
        return True
    if win_status == 'O':
        return True

assert not is_game_over('keep playing')
assert is_game_over('tie')
assert is_game_over('X')
assert is_game_over('O')

# Now that we've defined our functions, let's play a game of tic-tac-toe!

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
