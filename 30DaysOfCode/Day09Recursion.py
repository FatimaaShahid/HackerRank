#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    num=1
    if n==1:
        return 1
    else:
    
        num = n *factorial(n-1)
        return num
    # Write your code here
n=int(input())
num = 1
print(factorial(n))

