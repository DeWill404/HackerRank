#!/bin/python3

import sys

def isPrime(n):
	if n==2 or n==3:
		return True
	if n%2==0 or n%3==0:
		return False
	for i in range(5, int(n**0.5)+1, 6):
		if n%i==0 or n%(i+2)==0:
			return False
	return True


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())

	if isPrime(n):
		print(n)
	else:
		for i in range(int(n**0.5)+1, 1, -1):
			
			if n%i==0:
				a = isPrime(i)
				b = isPrime(n//i)
				
				if a and b: print(max(n//i, i))
				elif a: print(i)
				elif b: print(n//i)
				else: continue
				break