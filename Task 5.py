credit = int(input("Please provide CREDIT: "))
debit = int(input("Please provide DEBIT: "))
balance = credit - debit
if balance > 0:
    print(f"Balance is Positive and equals: {balance}")
elif balance < 0:
    print(f"Balance is Negative and equals: {balance}")
else:
    print("Company spends exactly the same about it earns")


