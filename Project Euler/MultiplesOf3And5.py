#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_3 = 3*(n//3)*(n//3+1)//2 - (n % 3 == 0)*n
    sum_5 = 5*(n//5)*(n//5+1)//2 - (n % 5 == 0)*n
    sum_15 = 15*(n//15)*(n//15+1)//2 - (n % 15 == 0)*n
    print(int(sum_3 + sum_5 - sum_15))