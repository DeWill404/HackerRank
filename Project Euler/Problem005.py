#!/bin/python3

import sys

def gcd(a, b):
	return gcd(b, a%b) if a%b else b

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	L = 1
	for i in range(1,n+1):
		L = (L*i)//gcd(L,i)
	print(L)