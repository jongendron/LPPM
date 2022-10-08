# Index slicing (more than one values)
# Extract all characters ...
# starting with X and up-to Y ...
# by steps of Z characters

parrot = "Norwegian Blue"
print()

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

print()

number = "9,223;372:036 854,775;807"    # 1 = start, 4 = slice step until end string --> ,,,,,,
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

