#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if len(s)> 0:
        count = 1
    else:
        count = 0
    for char in s:
        if char in alpha:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
