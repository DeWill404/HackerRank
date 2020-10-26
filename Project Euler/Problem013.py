# Enter your code here. Read input from STDIN. Print output to STDOUT
sum = 0

for _ in range(int(input())):
	sum += int(input())

print(str(sum)[:10])