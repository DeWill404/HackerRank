	#!/bin/python3

	import math
	import os
	import random
	import re
	import sys

	# Complete the sherlockAndAnagrams function below.
	def sherlockAndAnagrams(s):
		anag = 0
		map = {}
		
		for i in range(len(s)):
			for j in range(i,len(s)):
				s1 = ''.join(sorted(s[i:j+1]))
				map[s1] = map.get(s1, 0) + 1

		for key in map:
			anag += (map[key] - 1)*map[key]//2

		return anag

	if __name__ == '__main__':
		fptr = open(os.environ['OUTPUT_PATH'], 'w')

		q = int(input())

		for q_itr in range(q):
			s = input()

			result = sherlockAndAnagrams(s)

			fptr.write(str(result) + '\n')

		fptr.close()
