#!/bin/python3
n=int(input())
if n % 2!=0:
    print("Weird")
elif n % 2==0 and 2 <=n <= 5:
    print("Not Weird")
elif n % 2==0 and 6 <= n <=20:
    print("Weird")
elif n % 2==0 and 20<n:
    print("Not Weird")
