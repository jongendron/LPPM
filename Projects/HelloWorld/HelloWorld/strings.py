print("Today is a good day to learn Python")
print("Python is fun")
print("Python's string are easy to use")
print('We can event include "quotes" in strings')
print("hello" + " world")  # string concatination
greeting = "Hello"
name = "Bruce"

# if we want a space, we can add that too
print(greeting + name)
print(greeting + ' ' + name)

# if we want to enter the name to program
# name = input('Please enter your name ')
# print(greeting + ' ' + name)

# include age
name = "Jon"
age = 24
print(name,age)

# what type of variable
print("greeting:", type(greeting))
print("name:", type(name))
print("age:", type(age))

# watch the type change
age = 24
print(type(age))
age = "2 years"
print(type(age))

# concatanation can't mix string and int values
name = "Jon"
age = 24
print(name + " is " + age)

