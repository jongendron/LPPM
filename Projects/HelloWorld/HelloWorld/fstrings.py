# f strings (py 3.6 and greater)
# f"<strings>" specifies it is an f string
name = "Jon"
age = 26
print(name + f" is {age} years old") # can't concatenate int w/ str
print()

# Formating works the same with f strings
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")