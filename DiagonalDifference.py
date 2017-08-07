#!/bin/python3

import sys


n = int(input().strip())
prim = 0
sec = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    prim += a_t[a_i]
    sec += a_t[n-1-a_i]
print(abs(prim - sec))
