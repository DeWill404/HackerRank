# Enter your code here. Read input from STDIN. Print output to STDOUT

def getFactor(n):
	count = 1

	while n%2 == 0:
		count += 1
		n //= 2
	for i in range(3, int(n**0.5)+1, 2):
		temp = 1
		while n%i == 0:
			temp += 1
			n //= i
		count *= temp
	if n > 2:
		count *= 2

	return count


def genrateFactors(max_limit):
	factorList = {1:3}
	indexList = {2:2, 3:2}

	n = 3
	max_factor = 2
	cur_factor = 1

	while cur_factor < max_limit:
		n += 1
		cur_factor = getFactor(n)
		indexList[n] = cur_factor

		if n%2:
			cur_factor *= indexList[(n-1)//2]
		else:
			cur_factor = indexList[n//2] * indexList[n-1]
		
		if cur_factor > max_factor:
			for i in range(max_factor, cur_factor):
				factorList[i] = (n-1)*n//2
			max_factor = cur_factor

	return factorList


factorList = genrateFactors(1000)

for _ in range(int(input())):
	print( factorList[int(input())] )