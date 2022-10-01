class NaNError(Exception):
    def __init__(self, txt):
        self.txt = txt


def number_filter(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise NaNError(f'Error: {string} - is not a number')


input_txt = ''
counter = 1
numbers_list = []
print("Please input a single number. To abort please type 'stop'")
while input_txt != 'stop':
    try:
        input_txt = input(f"{counter}: ")
        numbers_list.append(number_filter(input_txt))
        counter += 1
    except NaNError as e:
        if input_txt != 'stop':
            print(e.txt)

print(f"Result list:\n{numbers_list}")