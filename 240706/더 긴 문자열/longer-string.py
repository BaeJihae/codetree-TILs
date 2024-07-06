n, m = input().split()

print(n, len(n)) if len(n) > len(m) else (print(m, len(m)) if len(n) < len(m) else print("same"))