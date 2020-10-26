#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
	prices.sort()
	s, e = 0, 1
	MAX = 1
	SUM = prices[0]
	while e<=len(prices) and s<e:
		while e<len(prices) and SUM+prices[e]<=k:
			SUM += prices[e]
			e += 1
		MAX = max(MAX,e-s)
		while e<len(prices) and s<e and SUM+prices[e]>k:
			s += 1
	return MAX

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	prices = list(map(int, input().rstrip().split()))

	result = maximumToys(prices, k)

	fptr.write(str(result) + '\n')

	fptr.close()
