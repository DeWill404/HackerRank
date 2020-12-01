#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
	n = int(input())
	b = bin(n)[2:]
	
	length = 0
	
	i = 0
	while i < len(b):
		j = i
		while j<len(b) and b[j]==b[i]:
			j += 1
		if j>i and j-i>length:
			length = j-i
		i = j
	
	print(length)
		