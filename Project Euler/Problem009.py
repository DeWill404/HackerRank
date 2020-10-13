#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
	n = int(input().strip())
	result = -1
	for a in range(1, n//3+1):
		b = (n*n - 2*n*a)//(2*n-2*a);
		c = n - a -b;
		if c*c == a*a + b*b:
			result = max(result, c*a*b)

	print(result)
