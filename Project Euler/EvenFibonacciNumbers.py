#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    prev = 1
    cur = 2
    tmp = 0
    sum = 2 if n >= 2 else 0    
    while cur + prev <= n:
        tmp = cur
        cur = cur + prev
        prev = tmp
        sum += cur * (cur % 2 == 0)
    print(sum)
        