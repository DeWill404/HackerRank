#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	occurence_count = [0]*26
	
	for i in a:
		occurence_count[ord(i)-97] += 1
	
	for i in b:
		occurence_count[ord(i)-97] -= 1
	
	return sum([abs(i) for i in occurence_count])

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	a = input()

	b = input()

	res = makeAnagram(a, b)

	fptr.write(str(res) + '\n')

	fptr.close()
