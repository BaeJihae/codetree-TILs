n, m = input().split()

num = 0

for i in range(int(n)):
    for j in range(int(m)):
        num += 1
        print(num, end = " ")
    print()