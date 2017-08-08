#!/usr/bin/python

def nextMove(r,c,y,x):
    if abs(x - c) > abs(y - r):
        if x > c:
            return "RIGHT"
        elif c > x:
            return "LEFT"
    else:
        if y > r:
            return "DOWN"
        elif r > y:
            return "UP"
    return ""

n = int(input())
r,c = [int(i) for i in input().strip().split()]
for i in range(0, n):
    row = input().strip()
    for j in range(0, n):
        if row[j] == 'p':
            princess_x = j
            princess_y = i

print(nextMove(r,c,princess_y,princess_x))
