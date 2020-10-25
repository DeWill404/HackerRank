# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

pattern = re.compile(r'https?://([a-zA-Z\-0-9.]+)')

domain_list = set()

for _ in range(int(input())):
	html = input()
	for domain in pattern.findall(html):
		I = domain.find(".")
		if domain and I!=-1:
			if domain[:I] in ["www",'ww2']:
				domain = domain[I+1:]
			domain_list.add(domain)

print(";".join(sorted(domain_list)))