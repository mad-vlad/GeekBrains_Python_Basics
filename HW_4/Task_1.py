from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Input work time: "))
    rate = int(input("Input rate: "))
    prize = int(input("Input prize: "))
    print((time_work * rate) + prize)