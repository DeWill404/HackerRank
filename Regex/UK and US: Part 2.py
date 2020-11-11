# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

line = [input().split() for _ in range(int(input()))]

l = lambda w,x: sum(i.count(w) for i in x)

for _ in range(int(input())):
    word = input()
    print(l(word, line)+l(re.sub("ou", "o", word), line))