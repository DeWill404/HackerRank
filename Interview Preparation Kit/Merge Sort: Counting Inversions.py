#!/bin/python3

import math
import os
import random
import re
import sys


def combine(arr, start, mid, end):
	swap = 0
	i, j = start, mid+1
	temp = []
	
	while i<=mid and j<=end:
		if arr[i] > arr[j]:
			swap += mid-i+1
			temp.append(arr[j])
			j += 1
		else:
			temp.append(arr[i])
			i += 1
			
	while i <= mid:
		temp.append(arr[i])
		i += 1
			
	while j <= end:
		temp.append(arr[j])
		j += 1
	
	for i in range(start, end+1):
		arr[i] = temp[i-start]
	
	return swap
	

def divide(arr, start, end, swap):
	if start < end:
		mid = (start+end)//2
		swap += divide(arr, start, mid, swap)+divide(arr, mid+1, end, swap)+combine(arr, start, mid, end)
	return swap


# Complete the countInversions function below.
def countInversions(arr):
	return divide(arr, 0, len(arr)-1, 0)
	

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input())

	for t_itr in range(t):
		n = int(input())

		arr = list(map(int, input().rstrip().split()))

		result = countInversions(arr)
		print(arr)

		fptr.write(str(result) + '\n')

	fptr.close()
