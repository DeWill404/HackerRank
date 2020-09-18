#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

	limit_dict = {}

	for a,b,k in queries:
		limit_dict[a-1] = limit_dict.setdefault(a-1, 0)+k
		limit_dict[b] = limit_dict.setdefault(b, 0)-k

	current = 0
	MAX = 0
	prev = 0

	for i in range(0,n+1):
		current = limit_dict.get(i,0) + prev
		prev = current
		MAX = max(current, MAX)
		
	return MAX

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nm = input().split()

	n = int(nm[0])

	m = int(nm[1])

	queries = []

	for _ in range(m):
		queries.append(list(map(int, input().rstrip().split())))

	result = arrayManipulation(n, queries)

	fptr.write(str(result) + '\n')

	fptr.close()
