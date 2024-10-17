# TODO: Write your name here.

import random

PLAYER = 'player'
COMPUTER = 'computer'


# Here are the empty functions that it's your job to implement!
# Check the assignment carefully to see what each function is supposed to do.
# Don't rename these functions! You can absolutely write extra functions aside from these
# ones if you want, but don't change the names of the five functions please.

def make_board():
    board = []
    for i in range(0, 9):
        board.append('')
    return board

def print_board(board):
    board_str = ''
    for board_index in range(0, len(board)):
        if board[board_index] == '':
            board_str += ' '
        else:
            board_str += board[board_index]

        if board_index % 3 == 2:
            board_str += '\n'
        else:
            board_str += ' | '
    print(board_str)

# we should maybe provide this function to the students
def row_column_to_board_index(row, col):
    return (row - 1) * 3 + col - 1

def valid_move(board, row_number, col_number):
    return row_number is not None and 1 <= row_number <= 3 and col_number is not None and 1 <= col_number <= 3 and board[row_column_to_board_index(row_number, col_number)] == ''

def get_player_move(board):
    while True:
        row_number = int(input('Input the row number where you would like to make your move (1-3): '))
        col_number = int(input('Input the column number where you would like to make your move (1-3): '))
        if not valid_move(board, row_number, col_number):
            print('Please input a valid board position!')
        else:
            break
    return row_column_to_board_index(row_number, col_number)

# simple computer algorithm to return a random empty location
def get_computer_move(board, computer_team):
    return random.choice([i for i in range(0, len(board)) if board[i] == ''])

def check_for_winner(board):
    win_conditions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6],
    ]

    winner = None
    for win_condition in win_conditions:
        winner_string = ''.join([board[index] for index in win_condition])
        if winner_string == 'XXX' or winner_string == 'OOO':
            winner = winner_string[0]
            break

    if winner is not None:
        return winner

    # empty spots and no winner yet
    if '' in board and winner is None:
        return 'keep playing'

    # all full but no winner is a tie
    if '' not in board and winner is None:
        return 'tie'

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

    # Decide who goes first.
    whose_turn = random.choice([PLAYER, COMPUTER])
    print('The {} will go first.'.format(whose_turn))

    # Get a fresh board.
    board = make_board()

    while True:
        # Figure out whose turn it is, and let them make a move.
        if whose_turn == PLAYER:
            print_board(board)
            index = get_player_move(board)
            print("You moved to board position: ", index)
            board[index] = player_team

        else:
            index = get_computer_move(board, computer_team)
            print("Computer moved to board position: ", index)
            board[index] = computer_team

        # Check to see if someone won, and end the game if so.
        win_status = check_for_winner(board)
        if win_status != 'keep playing':
            if win_status == 'tie':
                print('-------------------')
                print("It's a tie!")
                print_board(board)
                break
            else:
                print('-------------------')
                print('The {} wins!'.format(whose_turn))
                print_board(board)
                break

        # If we've made it this far, nobody's won yet, so let's get ready for the next turn.
        if whose_turn == PLAYER:
            whose_turn = COMPUTER
        else:
            whose_turn = PLAYER
