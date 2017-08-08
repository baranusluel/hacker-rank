#!/bin/python3

import sys


a_arr = [int(tmp) for tmp in input().strip().split(' ')]
b_arr = [int(tmp) for tmp in input().strip().split(' ')]
A = 0
B = 0
for i in range(0,3):
    if a_arr[i] > b_arr[i]:
        A += 1
    elif a_arr[i] < b_arr[i]:
        B += 1
print(str(A) + " " + str(B))

