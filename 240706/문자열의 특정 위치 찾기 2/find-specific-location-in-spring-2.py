word_list = ["apple", "banana", "grape", "blueberry", "orange"]

alphabet = input()
num = 0

for word in word_list:
    if word[2] == alphabet or word[3] == alphabet:
        num += 1
        print(word)

print(num)