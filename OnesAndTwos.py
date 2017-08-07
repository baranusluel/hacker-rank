#!/bin/python3

import sys

def getSums(a, b, results, offset):
    if a > 0:
        results.update(range(offset+1, offset+a+2*b+1)) # If at least one 1, every number until max sum
    else:
        results.update(range(offset+2, offset+2*b+1, 2)) # If no 1s, then only even numbers

test = set(range(0,5592406))
print(len(test))
n = int(input().strip())
for i in range(n):
    results = set()
    a,b = [int(tmp) for tmp in input().strip().split(' ')]
    try:
        getSums(a, b, results, 0)
    except:
        print("error1")
    print(len(results))
    for b_i in range(3,b+1):
        results.add(2**b_i)
        try:
            getSums(a, b-b_i, results, 2**b_i)
        except:
            print("error")
            print("Unexpected error:", sys.exc_info()[0])
        print(len(results))
    print(len(results) % (10**9+7))
    del(results)