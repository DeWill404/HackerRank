# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import re

c = re.compile(r'#include')
java = re.compile(r'import java.*?;')
python = re.compile(r'if (__name__ == \'__main__\'):')

INPUT = sys.stdin.read()

if c.search(INPUT):
	print("C")
elif java.search(INPUT):
	print("Java")
else:
	print("Python")