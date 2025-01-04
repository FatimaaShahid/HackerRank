t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    if n < 2:
        print("Not prime")
        continue

    flag = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not prime")
            flag = 1
            break

    if flag == 0:
        print("Prime")
