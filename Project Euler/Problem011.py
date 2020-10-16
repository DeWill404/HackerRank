#!/bin/python3

import sys


grid = []
result = 0
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
    for i in range(17):
        mul = 1
        for j in range(4):
            mul *= grid_t[i+j]
        result = max(mul, result)
    if grid_i >= 3:
        for i in range(20):
            mul = 1
            for j in range(4):
                mul *= grid[grid_i-j][i]
            result = max(mul, result)
        for i in range(17):
            mul = 1
            for j in range(4):
                mul *= grid[grid_i-j][i+j]
            result = max(mul, result)
        for i in range(3, 20):
            mul = 1
            for j in range(4):
                mul *= grid[grid_i-j][i-j]
            result = max(mul, result)

print(result)