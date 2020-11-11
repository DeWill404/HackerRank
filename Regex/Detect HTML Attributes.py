# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
import re
tag_with_attribute = re.compile(r'<\w+.*?>')
tag_name = re.compile(r'<(\w+)')
attributes = re.compile(r'(\w+)=".*?"')

d = defaultdict(set)

for _ in range(int(input())):
	tag = input()
	for tag in tag_with_attribute.findall(tag):
		name = tag_name.findall(tag)[0]
		d[name].add(0)
		for attr in attributes.findall(re.sub(r'\'', '"', tag)):
			d[name].add(attr)
			
for tag in sorted(d.keys()):
	d[tag].remove(0)
	print(tag+":"+",".join(sorted(d[tag])))