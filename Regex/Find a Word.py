# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

para = []
for _ in range(int(input())):
	para.append(input())

for _ in range(int(input())):
	word = input()
	pattern = re.compile(r'\b'+word+r'\b')
	print(sum(len(pattern.findall(sentences)) for sentences in para))