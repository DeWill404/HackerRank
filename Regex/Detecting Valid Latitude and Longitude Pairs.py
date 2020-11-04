# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = re.compile(r'\([+\-]?(90(\.0+)?|[1-8]?\d(\.\d+)?), [+\-]?(180(\.0+)?|(1[0-7]\d|[1-9]?\d)(\.\d+)?)\)')


for _ in range(int(input())):
	coordinate = input()
	print("Valid" if pattern.match(coordinate) else "Invalid")
