# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import re

pattern = re.compile(r'"/questions/(\d+).*?>(.*?)</a>.*?class="relativetime">(.*?)</span>', re.MULTILINE | re.DOTALL)

markup = sys.stdin.read()

for matches in pattern.findall(markup):
    print(";".join(matches))