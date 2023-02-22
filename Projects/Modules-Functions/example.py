# __'s indicate a variable is private to it's module
# but there are no true private variables
#print(dir())
#print()
#for m in dir(__builtins__):
#    print(m)

import shelve
print(dir())
print()
print(dir(shelve))
print()
print()

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
print()

#help(shelve)

import random
help(random.gauss)




