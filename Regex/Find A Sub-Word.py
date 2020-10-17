# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

para = [input() for _ in range(int(input()))]

for _ in range(int(input())):
	word = input()
	count = 0
	for line in para:
		count += len(re.findall("\w+"+word+"\w+",line))
	print(count)