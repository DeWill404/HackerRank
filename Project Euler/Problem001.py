#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	
	x = lambda a,b:(((a//b)*(a+b))>>1)-(a if a==n else 0)
	s = x(n-n%3,3)+x(n-n%5,5)-x(n-n%15,15)

	print(s)
