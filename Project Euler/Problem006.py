#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	natural_sum = (n*(n+1)//2)**2
	square_sum = n*(n+1)*(2*n+1)//6

	print( abs(natural_sum - square_sum) )