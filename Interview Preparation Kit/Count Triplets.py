#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
	rightCount = {}
	leftCount = {}

	for x in arr:
		rightCount[x] = rightCount.get(x,0)+1
	
	c = 0

	if r == 1:
		for i in rightCount:
			if rightCount[i] > 2:
				s = 0
				for j in range(1, rightCount[i]-1):
					s += j
					c += s
		return c

	for i in arr:
		leftCount[i] = leftCount.get(i,0)+1
		if i/r in leftCount and i*r in rightCount:
			c += leftCount[i//r]*(rightCount[i*r]-leftCount.get(i*r,0))

	return c


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nr = input().rstrip().split()

	n = int(nr[0])

	r = int(nr[1])

	arr = list(map(int, input().rstrip().split()))

	ans = countTriplets(arr, r)

	fptr.write(str(ans) + '\n')

	fptr.close()
