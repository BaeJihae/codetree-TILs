word_array = []

for _ in range(10):
    word_array.append(input())

alphabet = input()

for word in word_array:
    if word[-1] == alphabet:
        print(word)