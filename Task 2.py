time = int(input("Please provide time in seconds: "))

hours = 0
minutes = 0
while time > 3600:
    time = time - 3600
    hours += 1
print(hours)
while time > 60:
    time = time - 60
    minutes += 1
print(minutes)

print(f"The provided seconds are equal to this time [In format HH:MM:SS]: {hours}:{minutes}:{time}")