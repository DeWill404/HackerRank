#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
	count_dict = {}
	
	for i in s:
		count_dict[i] = count_dict.get(i,0)+1
	
	count_values = sorted(count_dict.values())
	SUM = sum(count_values)
	count_diff = lambda v : abs(SUM-v*(len(count_values)-1))
	
	return "YES" if count_values[0]==count_values[-1] or count_diff(count_values[0])==1 or count_diff(count_values[-1])==1 else "NO"

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	result = isValid(s)

	fptr.write(result + '\n')

	fptr.close()
