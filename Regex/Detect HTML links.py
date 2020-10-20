# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'<a href="(.*?)".*?>([\w ,./]*)(?=</)')

line = int(input())

for _ in range(line):
	string = input()
	for matches in pattern.findall(string):
		print(matches[0].strip()+","+matches[1].strip())
