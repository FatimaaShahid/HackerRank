

m=float(input())
tip=int(input())
tax=int(input())
i=(m / 100) * tip
j=(tax / 100) * m
print(round(m + i + j))
