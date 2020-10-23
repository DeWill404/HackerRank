# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'\b([\w+\.]+@(\w+\.)+\w+\b)')

email = set()

for _ in range(int(input())):
	line = input()
	for matches in pattern.findall(line):
		email.add(matches[0])

print(";".join(sorted(email)))