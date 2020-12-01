#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap = 0

for i in range(n):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            swap += 1

print(f"Array is sorted in {swap} swaps.")
print(f"First Element: {a[0]}")
print(f"Last Element: {a[-1]}")
