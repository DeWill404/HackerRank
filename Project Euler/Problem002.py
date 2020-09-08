#!/bin/python3

import sys

t = int(input().strip())
l = [int(input().strip()) for a0 in range(t)]

MAX = max(l)

f = [0,2]
while f[-1] <= MAX:
	f.append(4*f[-1]+f[-2])

for i in l:
	if f[-1] < i:
		print(sum(f))
	else:
		for j in range(len(f)):
			if f[j] >= i:
				print(sum(f[:j]))
				break
