# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    word = input()
    
    even = ""
    odd = ""
    
    for i in range(len(word)):
        if i%2:
            odd += word[i]
        else:
            even += word[i]
    
    print(even, odd)