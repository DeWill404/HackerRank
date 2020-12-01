#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    l = [i&(i-1) for i in range(2, 1000)]

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(k-1 if (k-1)|k <= n else k-2)
