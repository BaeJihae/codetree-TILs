arr_2nd = [list(map(int, input().split())) for _ in range(2)]

total_sum = 0

for arr in arr_2nd:
    sum = 0
    for i in arr:
        sum += i
    total_sum += sum
    print(sum / 4.0, end = " ")

print()

for i in range(4):
    sum = 0
    for j in range(2):
        sum = sum + arr_2nd[j][i]
    print(sum / 2.0, end = " ")

print()

print(total_sum / 8.0)