n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
num = 0

for col in range(n-1, -1, -1):
    if col % 2 != 0:
        for row in range(n-1, -1, -1):
            num += 1
            arr[row][col] = num
    else:
        for row in range(n):
            num += 1
            arr[row][col] = num

for a in arr:
    for i in a:
        print(i, end=" ")
    print()