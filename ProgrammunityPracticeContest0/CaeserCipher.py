#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    k = k % 26
    ans = ""
    for char in s:
        if char in alpha:
            ind = alpha.find(char)
            ans += alpha[(ind + k) % 26]
        elif char in alpha.upper():
            ind = alpha.upper().find(char)
            ans += alpha.upper()[(ind + k) % 26]
        else:
            ans += char
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
