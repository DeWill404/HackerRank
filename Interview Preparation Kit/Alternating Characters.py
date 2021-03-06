#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
	delete_count = 0
	
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			delete_count += 1
	
	return delete_count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	q = int(input())

	for q_itr in range(q):
		s = input()

		result = alternatingCharacters(s)

		fptr.write(str(result) + '\n')

	fptr.close()
