#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
	count_in_string = s.count('a')
	multiple_of_count = n//len(s)

	total_count = multiple_of_count * count_in_string
	if n%len(s):
		total_count += sum( 1 for i in range(n%len(s)) if s[i]=="a" )
	
	return total_count

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	n = int(input())

	result = repeatedString(s, n)

	fptr.write(str(result) + '\n')

	fptr.close()
