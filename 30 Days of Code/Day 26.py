# Enter your code here. Read input from STDIN. Print output to STDOUT

da, ma, ya = map(int, input().split())
d, m, y = map(int, input().split())

if ya < y:
    print(0)
elif ya == y:
    if ma < m:
        print(0)
    elif ma == m:
        if da <= d:
            print(0)
        else:
            print(15*(da-d))
    else:
        print(500*(ma-m))
else:
    print(10000)
