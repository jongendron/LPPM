a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76 # objects on right form a tuple
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76 # values on the right form a tuple
x, y, z = data # set values to each item of tuple
print(x)
print(y)
print(z)

print("Unpacking a list") # values can be unpacked form any seq type
data_list = [12, 13, 14]
# data_list.append(15) # causes a crash
print(data_list)
p, q, r = data_list # without the same number of variables as list it crashes
print(p)
print(q)
print(r)

# What if you change the values of list after it is unpacked?
# The values are not linked to the memory, they just absorbed it
print()
data_list[0] = 1
print(data_list)
print(p)
print(q)
print(r)

