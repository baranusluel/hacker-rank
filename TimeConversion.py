#!/bin/python3

import sys


time = input().strip()
type = time[-2:]
arr = [int(tmp) for tmp in time[:-2].split(':')]
if arr[0] == 12:
    arr[0] -= 12
arr[0] += 12 if type == "PM" else 0
zero = ""
if arr[0] < 10:
    zero = "0"
print(zero + str(arr[0]) + ":" + time[3:5] + ":" + time[6:8])