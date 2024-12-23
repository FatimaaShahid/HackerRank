#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    valid = 0
    low = 0
    cap = 0
    dig = 0
    special_char = 0
    
    for char in password:
        if char in lower_case:
            low = 1
        elif char in upper_case:
            cap = 1
        elif char in numbers:
            dig = 1
        elif char in special_characters:
            special_char = 1
    
    if low == 0:
        valid += 1
    if cap == 0:
        valid += 1
    if dig == 0:
        valid += 1
    if special_char == 0:
        valid += 1
    
    if len(password) + valid < 6:
        valid += 6 - (len(password) + valid)
    
    return valid

    
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
