# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
pattern = re.compile(r'^(_|\.)\d+([0a-zA-Z]+_)?$')

l = '''_0898989811abced_
_abce
_09090909abcD0'''.split("\n")

# for _ in range(int(input())):
#     name = input()
for name in l:
    if re.search(pattern, name):
        print("VALID")
    else:
        print("INVALID")