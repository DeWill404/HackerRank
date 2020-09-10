#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
	l = sorted(arr)
	print(sum(l[:-1]), sum(l[1:]))

if __name__ == '__main__':
	arr = list(map(int, input().rstrip().split()))

	miniMaxSum(arr)
