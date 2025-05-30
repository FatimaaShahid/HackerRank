#!/bin/python3

import math
import os
import random
import re
import sys



def compareTriplets(a, b):
    alice = 0
    bob = 0
    n = len(a)
    
    for i in range(n):
        if a[i]>b[i]:
            alice += 1
        elif a[i]<b[i]:
            bob += 1
        else:
            pass
    return [alice,bob]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
