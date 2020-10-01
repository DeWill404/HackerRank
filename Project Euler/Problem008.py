#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n,k = input().strip().split(' ')
	n,k = [int(n),int(k)]
	num = input().strip()

	product = 1
	for i in range(k):
		product *= int(num[i])
	
	MAX = product
	for i in range(k, n):
		if int(num[i-k]):
			product = product*int(num[i])//int(num[i-k])
		else:
			product = 1
			for j in range(i-k+1, i+1):
				product *= int(num[j])
		MAX = max(MAX, product)

	print(MAX)