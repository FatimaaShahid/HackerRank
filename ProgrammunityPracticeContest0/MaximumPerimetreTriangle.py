#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    maxp = 0
    ans = []
    sticks.sort()
    for a in range(len(sticks) - 2):
        for b in range(a + 1, len(sticks) - 1):
            for c in range(b + 1, len(sticks)):
                if sticks[a] + sticks[b] > sticks[c]:
                    perimeter = sticks[a] + sticks[b] + sticks[c]
                    if perimeter > maxp:
                        maxp = perimeter
                        ans = [sticks[a], sticks[b], sticks[c]]
    if ans:
        return ans
    return [-1]


                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
