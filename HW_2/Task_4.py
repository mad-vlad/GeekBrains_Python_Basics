string = input("Please inpud the sentence  ")
word = []
number = 1
for element in range(string.count(' ') + 1):
    word = string.split()
    if len(str(word)) <= 10:
        print(f" {number} {word [element]}")
        number += 1
    else:
        print(f" {number} {word [element] [0:10]}")
        number += 1