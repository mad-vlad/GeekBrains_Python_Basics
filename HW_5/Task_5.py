def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Please input numbers separated with space: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Error in file')
    except ValueError:
        print('Provided number is incorrect. Input-Output error')
summary()