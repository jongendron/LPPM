# About variable memory addresses during initialization
# and redefinition:
# https://medium.com/@daniel.tooke/variables-and-memory-addresses-in-python-6d96d672ed3d

class A():

    def __init__(self, name):
        self.name = name
        self.v1 = []


class B():

    def __init__(self, name, v2):
        self.name = name
        self.v2 = v2


a = A('obj_a')

v1 = a.v1

for i in range(3):
    v1.append(B('name'+str(i), i))

print(hex(id(v1)))
print(hex(id(a.v1)))

# Check that memory address is same
print(hex(id(v1)) == hex(id(a.v1))) # they are!

# This means that defining a variable as a class attribute of an instance
# creaters a pointer to that object
# This pointer lasts as long as the 
# object is not redefined

# For example v1 = [a.v1, 'one']
# this means v1 would no longer be a pointer,
# but rather element 1 of list v1,
# would point to a.v1

