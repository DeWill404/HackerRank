# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'^[a-z]{,3}[0-9]{2,8}[A-Z]{3,}$')

for _ in range(int(input())):
	id = input()
	print("VALID" if pattern.match(id) else "INVALID")