#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 

# Complete the freqQuery function below.
def freqQuery(queries):
	dsDict = {}
	output = []
	countDict = defaultdict(set)

	for option,value in queries:
		if option == 1:
			dsDict[value] = dsDict.setdefault(value,0)+1
			countDict[dsDict[value]-1].discard(value)
			countDict[dsDict[value]].add(value)
		elif option == 2:
			if dsDict.get(value,0) > 0:
				countDict[dsDict[value]].discard(value)
				dsDict[value] -= 1
				if dsDict[value] > 0:
					countDict[dsDict[value]].add(value)
		else:
			output.append(int(len(countDict[value])>0))

	return output



if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input().strip())

	q = []

	for _ in range(n):
		q.append(list(map(int, input().rstrip().split())))

	ans = freqQuery(q)

	fptr.write('\n'.join(map(str, ans)))
	fptr.write('\n')

	fptr.close()
