# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

ipv4_pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[\d]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[01]?[\d]{1,2})$')
ipv6_pattern = re.compile(r'^([\da-f]{1,4}:){7}[\da-f]{1,4}$')

for _ in range(int(input())):
	line = input()
	if ipv6_pattern.match(line):
		print("IPv6")
	elif ipv4_pattern.match( line):
		print("IPv4")
	else:
		print("Neither")
