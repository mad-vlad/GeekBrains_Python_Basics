def int_func(word: str):
    first_char = word[:1]
    big_first_char = first_char.upper()
    tail = word[1:]
    return big_first_char + tail


def int_func_ext(row: str):
    result = []
    words = row.split(' ')
    for item in words:
        result.append(int_func(item))
    return ' '.join(result)


s = input("Please input the line for transformation:\n")
print(f"{int_func_ext(s)}")