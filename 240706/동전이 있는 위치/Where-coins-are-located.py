n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j = tuple(map(int, input().split()))
    arr[i-1][j-1] = 1

for a in arr:
    for i in a:
        print(i, end = " ")
    print()