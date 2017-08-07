#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    factor = 2
    while factor <= n**0.5:
        while (n % factor == 0):
            n = n // factor
        if n == 1:
            continue
        if factor == 2:
            factor += 1
        else:
            factor += 2
    if n > 2:
        print(n)
    else:
        print(factor)