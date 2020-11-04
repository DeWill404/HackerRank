# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

pattern = re.compile(r'//.*|/\*[\S\s]*?\*/')

code = sys.stdin.read()

for matches in pattern.findall(code):
	print("\n".join(line.strip() for line in matches.split('\n')))