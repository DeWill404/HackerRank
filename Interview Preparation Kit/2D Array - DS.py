#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
	MAX = -(10**9)
	for i in range(4):
		for j in range(4):
			temp = sum(arr[i][k] for k in range(j,j+3) )
			temp += arr[i+1][j+1]
			temp += sum(arr[i+2][k] for k in range(j,j+3) )
			MAX = max(MAX, temp)
	return MAX

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	arr = []

	for _ in range(6):
		arr.append(list(map(int, input().rstrip().split())))

	result = hourglassSum(arr)

	fptr.write(str(result) + '\n')

	fptr.close()
