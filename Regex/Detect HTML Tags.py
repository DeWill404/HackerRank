# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'<(\w*).*?>')
tagList = []

line = int(input())

for _ in range(line):
	string = input()
	tagList += list(re.findall(pattern, string))

print(";".join(sorted(filter(None,set(tagList)))))
