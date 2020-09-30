#!/bin/python3

import sys

def seive(n):
    prime = list(range(3, n+1, 2))
    sl = len(prime)
    initial = 4

    for step in range(3, n+1, 2):
        for i in range(initial, sl+1, step):
            prime[i-1] = 0
        
        initial += 2*(step+1)
        if initial > sl:
            return [2] + list(filter(None, prime))

    return [2]


t = int(input().strip())
l = [int(input().strip()) for a0 in range(t)]

primeList = seive(max(l)*100)

for i in l:
    print( primeList[i-1] )