if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in reversed(arr):
        print(i,end=' ')
