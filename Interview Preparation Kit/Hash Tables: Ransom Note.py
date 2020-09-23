#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
	dict_magazine, dict_note = {}, {}
	
	for word in magazine:
		dict_magazine[word] = dict_magazine.setdefault(word, 0)+1
	for word in note:
		dict_note[word] = dict_note.setdefault(word, 0)+1

	for word in dict_note:
		if dict_magazine.get(word, 0) < dict_note[word]:
			print("No")
			return

	print("Yes")


if __name__ == '__main__':
	mn = input().split()

	m = int(mn[0])

	n = int(mn[1])

	magazine = input().rstrip().split()

	note = input().rstrip().split()

	checkMagazine(magazine, note)
