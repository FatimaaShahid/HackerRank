#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER v
#  2. 2D_INTEGER_ARRAY ships
#  3. 2D_INTEGER_ARRAY queries
#

from bisect import bisect_left, bisect_right
from collections import defaultdict

def solve(v, ships, queries):

    fighters = defaultdict(list)
    
    for x, y, f in ships:
        fighters[f].append(y)

    for f in fighters:
        fighters[f].sort()

    res = []

    for yu, yd, _ in queries:
        max_blocked = 0

        for y_list in fighters.values():
           
            start_index = bisect_left(y_list, yd)
           
            end_index = bisect_right(y_list, yu)
            
            ships_in_range = end_index - start_index
            max_blocked = max(max_blocked, ships_in_range)
        
        
        res.append(max_blocked)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])
    v = int(first_multiple_input[2])

    ships = [list(map(int, input().rstrip().split())) for _ in range(n)]
    queries = [list(map(int, input().rstrip().split())) for _ in range(q)]

    result = solve(v, ships, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

