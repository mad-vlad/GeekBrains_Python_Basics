n = int(input("Please provide a positive integer number:  "))
max = 0
while n > 0:
    if ((n % 10) > max):
        max = n % 10
    n = n // 10
    print("n= ",n)
print(f"Highest number in provide is: {max}")