#!/bin/python3

import sys

def isProduct(n):
	for i in range(100, 1000):
		if n%i==0 and n//i>99 and n//i<1000:
			return True
	return False

isPalindrome = lambda x: str(x)==str(x)[::-1]

t = int(input().strip())
for a0 in range(t):
	N = int(input().strip())-1

	while True:
		if isPalindrome(N):
			if isProduct(N):
				print(N)
				break
		N -= 1