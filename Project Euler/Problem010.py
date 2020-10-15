#!/bin/python3

import sys


def seive(n):
	prime = [1]*(n+1)
	prime[0] = prime[1] = 0

	for i in range(2, int(n**0.5)+1):
		if prime[i]:
			for j in range(i*i, n+1, i):
				prime[j] = 0
	
	for i in range(1, n+1):
		prime[i] = i*prime[i]+prime[i-1]

	return prime


t = int(input().strip())
l = [int(input()) for i in range(t)]

primeList = seive(max(l))
for i in l:
	print(primeList[i])
