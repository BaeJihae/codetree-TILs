arr_2nd = [list(map(int, input().split())) for i in range(4)]

for arr in arr_2nd:
    sum = 0
    for i in arr:
        sum += i
    print(sum)