# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'^[_.]\d+[a-zA-Z]*_?$')


for _ in range(int(input())):
    name = input()
    if pattern.search(name):
        print("VALID")
    else:
        print("INVALID")
