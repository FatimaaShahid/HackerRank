#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zero = 0
    
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    
    # Correct the print statements to display the ratios with 6 decimal places
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zero/n:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
