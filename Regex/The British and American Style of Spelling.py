# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'(\b\w*(ze|se)\b)')

word = []
for _ in range(int(input())):
    line = input()
    for w in pattern.findall(line):
        word.append(re.sub(r'se\b', 'ze', w[0]))

for _ in range(int(input())):
    print(word.split().count(input()))