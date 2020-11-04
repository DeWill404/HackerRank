# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'hackerrank', re.IGNORECASE)

count = 0

for _ in range(int(input())):
	tweets = input()
	if pattern.search(tweets):
		count += 1
		
print(count)