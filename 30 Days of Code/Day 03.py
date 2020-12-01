#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
	N = int(input())

	print("Weird" if N%2 or (N%2==0 and N>=6 and N<=20) else "Not Weird")