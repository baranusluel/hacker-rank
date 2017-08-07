#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos,zero,neg = [0,0,0]
for i in range(n):
    if arr[i] < 0:
        neg += 1
    elif arr[i] == 0:
        zero += 1
    else:
        pos += 1
print(pos/n)
print(neg/n)
print(zero/n)