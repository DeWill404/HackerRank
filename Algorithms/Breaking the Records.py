#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
	best_count = 0
	worst_count = 0
	best_score = scores[0]
	worst_score = scores[0]

	for i in range(1,len(scores)):
		if scores[i] > best_score:
			best_score = scores[i]
			best_count += 1
		elif scores[i] < worst_score:
			worst_score = scores[i]
			worst_count += 1

	return best_count,worst_count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	scores = list(map(int, input().rstrip().split()))

	result = breakingRecords(scores)

	fptr.write(' '.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
