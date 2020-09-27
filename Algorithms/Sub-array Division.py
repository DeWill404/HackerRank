#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
	count = 0
	
	if len(s) < m:
		return 0

	SUM = sum(s[:m])
	if SUM==d:
		count += 1
	for i in range(m, len(s)):
		SUM += s[i]-s[i-m]
		if SUM == d:
			count += 1

	return count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	s = list(map(int, input().rstrip().split()))

	dm = input().rstrip().split()

	d = int(dm[0])

	m = int(dm[1])

	result = birthday(s, d, m)

	fptr.write(str(result) + '\n')

	fptr.close()
