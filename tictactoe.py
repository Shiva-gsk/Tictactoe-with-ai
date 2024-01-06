"""
Tic Tac Toe Player
"""

import copy
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
    countX = 0
    countO = 0
    
    for row in board:
        for column in row:
            if column == "X":
                countX += 1
            elif column == "O":
                countO += 1

    if countX > countO:
        return O
    else:
        return X                
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    all_actions = set()

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == None:
                all_actions.add((row, column))

    return all_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = action
    if player_move not in actions(board):
        raise ValueError(f"You can't make this move")
    row , column = player_move
    new_board = copy.deepcopy(board)
    new_board[row][column] = player(board)

    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        x_row = True
        o_row = True

        for xo in row: 
            if xo != X:
                x_row = False
            if xo != O:
                o_row = False

        if x_row:
            return X
        if o_row:
            return O

    for column in range(len(board[0])):
        x_column = True
        o_column = True

        for row in range(len(board)):
            cell = board[row][column]

            if cell != X:
                x_column = False
            if cell != O:
                o_column = False

        if x_column:
            return X
        if o_column:
            return O

    diagnol_1 = {board[0][0] , board[1][1] , board[2][2]}             
    diagnol_2 = {board[0][2] , board[1][1] , board[2][0]}
    if diagnol_1 == {X} or diagnol_2 == {X}:
        return X
    if diagnol_1 == {O} or diagnol_2 == {O}:
        return O

    return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if len(actions(board)) ==0:
        return True
    elif winner(board) != None:
        return True
    else: 
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    raise Exception("Error of utility")

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    def max_value(board):
        if terminal(board):
            return utility(board), None
        
        v = float('-inf')
        
        best_action = None

        for action in actions(board):

            min_v , _ = min_value(result(board, action))
            
            if min_v > v:
                v = min_v
                best_action = action

        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        
        v = float('inf')
        
        best_action = None
        for action in actions(board):

            max_v, _ = max_value(result(board, action))

            if max_v < v:
                v = max_v
                best_action = action
        
        return v, best_action
    
    if player(board) == X:
        _, best_move = max_value(board)

    else:
        _, best_move = min_value(board)

    return best_move        