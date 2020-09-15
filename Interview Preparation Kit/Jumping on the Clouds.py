#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	COUNT = 0
	i = 0
	while i+1<len(c):
		if i+2 < len(c) and c[i+2]==0:
			i += 2
		else:
			i += 1
		COUNT += 1
	return COUNT

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	c = list(map(int, input().rstrip().split()))

	result = jumpingOnClouds(c)

	fptr.write(str(result) + '\n')

	fptr.close()
