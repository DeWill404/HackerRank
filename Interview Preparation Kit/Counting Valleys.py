#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	c = 0
	COUNT = 0
	for i in s:
		t = c-1 if i=="D" else c+1
		if c==0 and t==-1:
			COUNT += 1
		c = t
	return COUNT

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	s = input()

	result = countingValleys(n, s)

	fptr.write(str(result) + '\n')

	fptr.close()
