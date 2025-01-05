#!/bin/python3

import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    s = sum(arr) 
    max_s = s - min(arr)
    min_s = s - max(arr)
    print(min_s,max_s)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
