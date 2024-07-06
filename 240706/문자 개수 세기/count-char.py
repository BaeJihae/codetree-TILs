str = input()
word = input()

num = 0

for a in str:
    if a == word:
        num += 1

print(num)