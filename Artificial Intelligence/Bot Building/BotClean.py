#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        return "CLEAN"
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

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))
