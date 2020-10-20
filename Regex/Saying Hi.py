# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'^[Hh][Ii]\s[^Dd].*$')

line = int(input())

for _ in range(line):
	string = input()
	if (pattern.match(string)):
		print(string)