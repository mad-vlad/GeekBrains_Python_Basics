list = [5, 4, 3, 2, 1]
print(f"Rating - {list}")
digit = int(input("Please input the number (000 - to exit) "))
while digit != 000:
    for el in range(len(list)):
        if list[el] == digit:
            list.insert(el + 1, digit)
            break
        elif list[0] < digit:
            list.insert(0, digit)
        elif list[-1] > digit:
            list.append(digit)
        elif list[el] > digit and list[el + 1] < digit:
            list.insert(el + 1, digit)
    print(f"current list - {list}")
    digit = int(input("Please input the number (000 - to exit) "))