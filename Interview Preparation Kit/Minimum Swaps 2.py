#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	swap_count = 0

	pair_dict = dict( zip(arr, range(1,len(arr)+1)) )

	for i in range(1, len(arr)+1):
		if pair_dict[i] != i:
			arr[pair_dict[i]-1] = arr[i-1]
			pair_dict[i],pair_dict[arr[i-1]] = pair_dict[arr[i-1]],pair_dict[i]
			arr[i-1] = i
			swap_count += 1

	return swap_count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	res = minimumSwaps(arr)

	fptr.write(str(res) + '\n')

	fptr.close()
