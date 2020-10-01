#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
	date = [13,"09",str(year)]

	if year > 1918:
		if (year%400==0) or (year%4==0 and year%100!=0):
			date[0] -= 1
	elif year == 1918:
		date[0] = 26
	else:
		if year%4 == 0:
			date[0] -= 1

	date[0] = str(date[0])

	return ".".join(date)


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	year = int(input().strip())

	result = dayOfProgrammer(year)

	fptr.write(result + '\n')

	fptr.close()
