#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    students = 0
    for i in range(n):
        if a[i] <= 0:
            students += 1
    if students < k:
        print("YES")
    else:
        print("NO")
