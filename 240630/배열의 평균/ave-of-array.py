arr_2nd = [list(map(int, input().split())) for _ in range(2)]

total_sum = 0

for i in range(2):
    sum = 0
    for j in range(4):
        sum = sum + arr_2nd[i][j]
    total_sum += sum
    print(round(sum / 4.0, 1), end = " ")

print()

for i in range(4):
    sum = 0
    for j in range(2):
        sum = sum + arr_2nd[j][i]
    print(round(sum / 2.0, 1), end = " ")

print()

print(round(total_sum / 8.0, 1))