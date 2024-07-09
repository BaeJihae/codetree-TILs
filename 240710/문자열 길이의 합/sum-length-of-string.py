n = int(input())

sum = 0

count_a = 0

for _ in range(n):
    str = input()
    if str[0] == "a":
        count_a += 1
    sum += len(str)

print(sum, count_a)