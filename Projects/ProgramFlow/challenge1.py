# Write program to ask for a name and an age
# When both values have been entered ...
# check if the person is the right age to go on an 18-30 holiday
# This means over 18 and under 31

name = input("What is your name? ")
print()
age = int(input("What is your age? "))
print()

if 18 <= age <= 30:
    print("{0}, since you are {1} you can go on this holiday"
          .format(name, age))
elif age < 18:
    print("{0}, you are {1} year(s) too young for this holiday"
          .format(name, 18 - age))
else:
    print("{0}, you are {1} year(s) too old for this holiday"
    .format(name, age - 30))
