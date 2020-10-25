#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
	s = 0
	for i in range(len(bill)):
		if i != k:
			s += bill[i]
	s //= 2

	if s == b:
		print("Bon Appetit")
	else:
		print(bill[k]//2)


if __name__ == '__main__':
	nk = input().rstrip().split()

	n = int(nk[0])

	k = int(nk[1])

	bill = list(map(int, input().rstrip().split()))

	b = int(input().strip())

	bonAppetit(bill, k, b)
