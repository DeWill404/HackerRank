#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
	no_of_apple, no_of_orange = 0, 0

	for A in apples:
		if a+A >=s and a+A<=t:
			no_of_apple += 1

	for O in oranges:
		if b+O >=s and b+O<=t:
			no_of_orange += 1

	print(no_of_apple)
	print(no_of_orange)

if __name__ == '__main__':
	st = input().split()

	s = int(st[0])

	t = int(st[1])

	ab = input().split()

	a = int(ab[0])

	b = int(ab[1])

	mn = input().split()

	m = int(mn[0])

	n = int(mn[1])

	apples = list(map(int, input().rstrip().split()))

	oranges = list(map(int, input().rstrip().split()))

	countApplesAndOranges(s, t, a, b, apples, oranges)
