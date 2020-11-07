#!/bin/python3

import math
import os
import random
import re
import sys

def getMedian(E, d):
	l = []
	count = 0
	m1, m2 = d//2, d//2+1
	
	for i,c in enumerate(E):
		count += c
		if not l and count>=m1:
			l.append(i)
		if count >= m2:
			l.append(i)
			break
	
	return l[-1]*2 if d%2 else sum(l)

	
# Complete the activityNotifications function below.
def activityNotifications(exp, d):
	if len(exp) <= d:
		return 0
	
	count = 0
	exp_count = [0]*201
	for i in range(d):
		exp_count[exp[i]] += 1
	
	for i in range(d, len(exp)):
		median = getMedian(exp_count, d)
		if exp[i] >= median:
			count += 1
		exp_count[exp[i]] += 1
		exp_count[exp[i-d]] -= 1
	
	return count

		
if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nd = input().split()

	n = int(nd[0])

	d = int(nd[1])

	expenditure = list(map(int, input().rstrip().split()))

	result = activityNotifications(expenditure, d)

	fptr.write(str(result) + '\n')

	fptr.close()
