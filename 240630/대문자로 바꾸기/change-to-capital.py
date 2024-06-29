arrs = [list(map(str, input().split())) for _ in range(5)]

for arr in arrs:
    for a in arr:
        print(a.upper(), end = " ")
    print()