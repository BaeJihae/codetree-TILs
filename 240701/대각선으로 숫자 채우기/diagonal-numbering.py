n, m = map(int, input().split())

list = [[0 for _ in range(m)] for _ in range(n)]

row, col = 0, 0
num = 1

for i in range(n+m-1):
    row, col = 0, i
    for _ in range(i+1):
        if row < m and col < n:
            list[row][col] = num
            num += 1
        row += 1
        col -= 1

for arr in list:
    for i in arr:
        print(i, end=" ")
    print()