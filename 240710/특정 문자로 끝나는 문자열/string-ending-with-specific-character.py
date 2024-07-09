word_array = []

for _ in range(10):
    word_array.append(input())

alphabet = input()
num = 0

for word in word_array:
    if word[-1] == alphabet:
        print(word)
        num += 1

if num == 0:
    print("None")