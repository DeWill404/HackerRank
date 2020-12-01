class Calculator:
    def __init__(self):
        pass

    def power(self, b, p):
        if b<0 or p<0:
            raise Exception("n and p should be non-negative")
        return b**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
