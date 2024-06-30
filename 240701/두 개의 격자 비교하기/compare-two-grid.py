n, m = map(int, input().split())

arr1_2d = [list(map(int, input().split())) for _ in range(n)]
arr2_2d = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr1_2d[i][j] == arr2_2d[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()