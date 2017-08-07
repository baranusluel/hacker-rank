#!/bin/python3

import sys

E = 100
i = 0
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
while E > 0:
    i = (i + k) % n
    E -= 1
    if c[i] == 1:
        E -= 2
    if i == 0:
        break
print(E)