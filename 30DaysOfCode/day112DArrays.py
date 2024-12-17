#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))




def get_max_hour_glass_sum(arr):
    result = -math.inf
    for row in range(4):
        for col in range(4):
            hour_glass_sum = \
                arr[row][col] + arr[row][col+1] + arr[row][col+2] + \
                arr[row+1][col+1] + \
                arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            result = max((result, hour_glass_sum))
    print(result)
        
        
get_max_hour_glass_sum(arr)       
 
