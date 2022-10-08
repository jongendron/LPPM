day = "Friday"
temperature = 30
raining = False

# and has higher precedence than or, but its easier to read with ()'s
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")