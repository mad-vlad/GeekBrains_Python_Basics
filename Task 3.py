n = int(input("Please provide a number: "))
decs = n * 10
hundr = n * 100
sum = n + (decs + n) + (hundr + decs + n)

print(f"Provided number is {n} and in calculation {n}+{decs+n}+{hundr+decs+n} it equels: {sum}")