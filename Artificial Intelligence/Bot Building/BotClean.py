#!/usr/bin/python

from copy import copy, deepcopy

def next_move(posr, posc, board):
    if game_simulator(posr, posc, deepcopy(board), True) < game_simulator(posr, posc, deepcopy(board), False):
        return next_move_rows(posr, posc, board)
    else:
        return next_move_columns(posr, posc, board)
    
def game_simulator(posr, posc, board, usingRows):
    count = 0
    while (True):
        dir = next_move_rows(posr, posc, board) if usingRows else next_move_columns(posr, posc, board)
        if dir == "CLEAN":
            board[posr][posc] = "b"
        else:
            board[posr][posc] = "-"
            if dir == "RIGHT":
                posc += 1
            elif dir == "LEFT":
                posc -= 1
            elif dir == "UP":
                posr -= 1
            elif dir == "DOWN":
                posr += 1
            if (posr > 4 or posc > 4):
                break
            if board[posr][posc] == "-":
                board[posr][posc] = "b"
        count += 1
    return count

# Output the state of the board, used for debugging
def print_board(board):
    for i in range(5):
        print(board[i])

# Next move function for column-by-column strategy
def next_move_columns(posr, posc, board):
    if board[posr][posc] == 'd':
        return "CLEAN"
    for x in range(posc):
        for y in range(5):
            if board[y][x] == 'd':
                return "LEFT"
    target_r = []
    for i in range(5):
        if board[i][posc] == 'd':
            target_r.append(i)
    if len(target_r) == 0:
        return "RIGHT"
    else:
        min_r = -1
        min_r_dist = 5
        for i in range(len(target_r)):
            if abs(target_r[i] - posr) < min_r_dist:
                min_r = target_r[i]
                min_r_dist = abs(target_r[i] - posr)
        if min_r > posr:
            return "DOWN"
        else:
            return "UP"
    return ""

# Next move function for row-by-row strategy
def next_move_rows(posr, posc, board):
    if board[posr][posc] == 'd':
        return "CLEAN"
    for y in range(posr):
        for x in range(5):
            if board[y][x] == 'd':
                return "UP"
    target_c = []
    for i in range(5):
        if board[posr][i] == 'd':
            target_c.append(i)
    if len(target_c) == 0:
        return "DOWN"
    else:
        min_c = -1
        min_c_dist = 5
        for i in range(len(target_c)):
            if abs(target_c[i] - posc) < min_c_dist:
                min_c = target_c[i]
                min_c_dist = abs(target_c[i] - posc)
        if min_c > posc:
            return "RIGHT"
        else:
            return "LEFT"
    return ""

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
