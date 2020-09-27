#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
	bird_dict = {}
	
	for i in arr:
		bird_dict[i] = bird_dict.setdefault(i, 0)+1
	
	key_list = sorted(bird_dict)

	return max(key_list, key=lambda x:bird_dict[x])

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	arr_count = int(input().strip())

	arr = list(map(int, input().rstrip().split()))

	result = migratoryBirds(arr)

	fptr.write(str(result) + '\n')

	fptr.close()
