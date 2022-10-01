class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def smart_divider(a, b):
    if b == 0:
        raise DivisionByZeroError(f'{a} / {b} = Division By Zero Error!')
    return a / b


try:
    smart_divider(6, 0)
except DivisionByZeroError as e:
    print(e)

print(f"45 / 5 = {smart_divider(45, 5)}")