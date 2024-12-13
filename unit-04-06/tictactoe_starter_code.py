# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'


# Here are the empty functions that it's your job to implement!
# Check the assignment carefully to see what each function is supposed to do.
# Don't rename these functions! You can absolutely write extra functions aside from these
# ones if you want, but don't change the names of the six functions please.

# Plan: What is make board supposed to output?
def make_board():
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass

assert make_board() == [['', '', ''], ['', '', ''], ['', '', '']]


def print_board(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass

# We're expecting the following code to output
#
# Printing an empty board
# |   |   |   |
# |   |   |   |
# |   |   |   |
# Printing an example board
# | X |   | O |
# | O | X | X |
# | X |   | O |
print('Printing an empty board')
print_board(make_board())
print('Printing an example board')
print_board([
  ['X', '', 'O'],
  ['O', 'X', 'X'],
  ['X', '', 'O']
])
# Write your output in the comment below:
#
#
#
# Does it match what we're expecting?

def get_player_move(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass
print('Try running get_player_move with the input of row number 3 and col number 2')
assert get_player_move(make_board()) == (2, 1)

# What is the expectation for get_computer_move?
def get_computer_move(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass
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
        # diagnol across left to right win condition
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
assert len(get_win_conditions()) == 8

def did_turn_win(whose_turn, board, win_condition):
    pass
assert did_turn_win('X', [['X', 'X', 'X'], ['O', '', 'O'], ['', 'O', '']], [[0, 0], [0, 1], [0, 2]])
assert not did_turn_win('O', [['X', 'X', 'X'], ['O', '', 'O'], ['', 'O', '']], [[0, 0], [0, 1], [0, 2]])
assert did_turn_win('O', [['O', 'O', 'O'], ['X', '', 'X'], ['', 'X', '']], [[0, 0], [0, 1], [0, 2]])

def get_game_status(board, winner):
    pass
assert get_game_status(make_board(), None) == 'keep playing'
assert get_game_status(make_board(), 'X') == 'X'
assert get_game_status(make_board(), 'O') == 'O'
assert get_game_status([
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', 'X']
], None) == 'tie'

def check_for_winner(board):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    # You will use get_win_conditions, did_turn_win, and get_game_status in this function
    pass
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

# What argument are we giving to is_game_over?
# What are the possible values for that argument? Take a look at the assert statements below
# What kind of value are we expecting is_game_over to return?
def is_game_over(win_status):
    # TODO: remove this comment and the `pass` line below it once you've written some code in this function.
    pass
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
