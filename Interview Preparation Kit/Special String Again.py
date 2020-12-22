#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
	special_count = len(s)

	for i in range(len(s)):
		j = i+1
		while j<len(s) and s[i]==s[j]:
			special_count += 1
			j += 1
		if  i>0 and i<len(s)-1 and s[i]!=s[i+1]:
			j,k = i-1,i+1
			while j>=0 and k<len(s) and s[j]==s[i+1] and s[k]==s[i+1]:
				special_count += 1
				j -= 1
				k += 1
		
	return special_count
	

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	s = input()

	result = substrCount(n, s)

	fptr.write(str(result) + '\n')

	fptr.close()
