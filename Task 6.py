credit = int(input("Please provide CREDIT in thousands USD: "))
debit = int(input("Please provide DEBIT  in thousands USD: "))
balance = credit - debit
employees = 0
if balance > 0:
    print(f"Balance is Positive and equals: {balance}k USD")
    print(f"Profitability: {(balance / credit) * 100} %")
    employees = int(input("Please provide number of employees: "))
    print(f"Profit per employee for this company is {balance/employees}")
elif balance < 0:
    print(f"Balance is Negative and equals: {balance} k USD")
else:
    print("Company spends exactly the same about it earns")


