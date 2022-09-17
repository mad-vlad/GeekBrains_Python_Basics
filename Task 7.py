a = int(input("Please provide Result from the first day in KM: "))
b = int(input("Please provide the result you would liket o achive: "))
i = 1
while a < b:
    a = a + (a * (1/10))
    print("A = ",a)
    i += 1
print(f"It will take {i} days to run for {b} KMs")