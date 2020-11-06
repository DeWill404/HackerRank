# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]')

for _ in range(int(input())):
	pan = input()
	print("YES" if pattern.match(pan) else "NO")