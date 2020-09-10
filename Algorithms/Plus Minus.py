#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
	p,n,z = 0,0,0
	for i in arr:
		if i > 0:
			p += 1
		elif i < 0:
			n += 1
		else:
			z += 1
	for i in [p/len(arr), n/len(arr), z/len(arr)]:
		print(i)

if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	plusMinus(arr)
