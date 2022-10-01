element_number = int(input('Please input how many elements you will prpovide: '))
list = []
i = 0
el = 0
while i < element_number:
    list.append(input('Please input next element: '))
    i += 1

for elem in range(int(len(list)/2)):
    list[el] , list[el+1] = list[el+1] , list[el]
    el+=2

print (list)


