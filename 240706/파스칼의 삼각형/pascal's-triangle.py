n = int(input())

arr = [[1 for _ in range(1, i+1)] for i in range(1, n+1)]

for i in range(1, n):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for a in arr:
    for i in a:
        print(i, end = " ")
    print()