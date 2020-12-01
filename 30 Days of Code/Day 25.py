# Enter your code here. Read input from STDIN. Print output to STDOUT

def prime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    
    for i in range(5, int(n**0.5)+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    
    return True


for _ in range(int(input())):
    n = int(input())
    print("Prime" if prime(n) else "Not prime")
