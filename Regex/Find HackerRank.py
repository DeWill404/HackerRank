# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern_startswith = re.compile(r'^hackerrank', re.IGNORECASE)
pattern_endswith = re.compile(r'hackerrank$', re.IGNORECASE)

for _ in range(int(input())):
	convo = input()
	if pattern_startswith.search(convo) and pattern_endswith.search(convo):
		print(0)
	elif pattern_startswith.search(convo):
		print(1)
	elif pattern_endswith.search(convo):
		print(2)
	else:
		print(-1)