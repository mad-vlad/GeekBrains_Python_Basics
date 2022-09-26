list_of_seasons = ['winter', 'spring', 'summer', 'autumn']
dict_of_seasons = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}
month = int(input("Please input the month Number: "))
if month ==12 or month == 1 or month == 2:
    print(dict_of_seasons.get(1))
    print(list_of_seasons[0])
elif month == 3 or month == 4 or month ==5:
    print(dict_of_seasons.get(2))
    print(list_of_seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(dict_of_seasons.get(3))
    print(list_of_seasons[2])
elif month == 9 or month == 10 or month == 11:
    print(dict_of_seasons.get(4))
    print(list_of_seasons[3])
else:
    print("There is no such a month")