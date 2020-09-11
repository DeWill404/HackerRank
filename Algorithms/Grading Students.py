#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
	for i in range(len(grades)):
		t = grades[i]
		while t%5:
			t += 1
		if t>=40 and t-grades[i] not in [0,3,4]:
			grades[i] = t
	return grades


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	grades_count = int(input().strip())

	grades = []

	for _ in range(grades_count):
		grades_item = int(input().strip())
		grades.append(grades_item)

	result = gradingStudents(grades)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
