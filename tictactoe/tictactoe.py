"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_cnt, o_cnt = 0, 0
    for i_line in board:
        for element in i_line:
            if element == O:
                o_cnt += 1
            elif element == X:
                x_cnt += 1
    if x_cnt <= o_cnt:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i, i_line in enumerate(board):
        for j, element in enumerate(i_line):
            if element == EMPTY:
                action_set.add((i, j))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)

    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(new_board)
        return new_board
    raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """


    # Checking diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY:
        return board[0][2]

    # Checking rows
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

    # Checking columns
    for col in range(0, 3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If someone already won
    if winner(board):
        return True

    # Check if there are still possible actions
    # TODO: think of using actions
    for i in board:
        for j in i:
            if j == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)
    if the_winner == X:
        return 1
    elif the_winner == O:
        return -1
    else:
        return 0


# Ideas: if I found 1 or 0 I should terminate!
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    val = -99
    the_action = None
    for action in actions(board):
        temp = min_value(result(board, action))
        if val < temp:
            the_action = action
            val = temp

    return the_action


def max_value(board):
    max_v = -99
    if terminal(board):
        return utility(board)

    for action in actions(board):
        max_v = max(min_value(result(board, action)), max_v)
        if max_v == 1:
            return 1


    return max_v


def min_value(board):
    min_v = +99
    if terminal(board):
        return utility(board)
    for action in actions(board):
        min_v = min(max_value(result(board, action)), min_v)
        if min_v == -1:
            return -1
    return min_v
