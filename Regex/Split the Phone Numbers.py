# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'(\d{1,3})\s?-?(\d{1,3})\s?-?(\d{4,10})')

for _ in range(int(input())):
    number = input()
    CC,LAC,NUM = pattern.findall(number)[0]
    print(f"CountryCode={CC},LocalAreaCode={LAC},Number={NUM}")