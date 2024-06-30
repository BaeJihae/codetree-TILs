n = int(input())
num = 0
arr = []
 
for i in range(n):
    arr_tmp = []
    for j in range(n):
        arr_tmp.append(0)
    arr.append(arr_tmp)
    
for i in range(n):
    for j in range(n):
        num += 1
        arr[j][i] = num

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()