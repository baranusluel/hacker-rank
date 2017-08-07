#!/bin/python3

import sys
import re

s = input().strip()
n = 0
for i in range(0,len(s)-3):
    a = s[i]
    for j in range(i+1,len(s)-2):
        b = s[j]
        c_i = [m.start()+j+1 for m in re.finditer(b, s[j+1:])]
        if len(c_i) == 0:
            continue
        for k in c_i:
            d_i = [m.start() for m in re.finditer(a, s[k+1:])]
            n += len(d_i)
print(n)