# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

STDIN = sys.stdin.read().split("\n")

n = int(STDIN[0])

d = {}
for i in range(1,n+1):
    name, number = STDIN[i].split()
    d[name] = number

for name in STDIN[n+1:]:
    if name in d:
        print(name+"="+d[name])
    else:
        print("Not found")
