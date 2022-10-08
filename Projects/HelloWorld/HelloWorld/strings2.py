#
#        012345678910111213
parrot = "Norweigan Blue"

print(parrot)

print(parrot[3])    # indicies start at 0 -> [3] indexes fourth elem
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[5])
print(parrot[8])

print()

print(parrot[-1])   # counts from end of string (starts from -1 not 0)
print(parrot[-14])

# write we win but with negative indexes string length - pos index
print()
print(parrot[3 - 14])    # indicies start at 0 -> [3] indexes fourth elem
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[5 - 14])
print(parrot[8 - 14])

# Slices
print()

print(parrot[0:6])  # slice index from 0 up-to but not including 6 (Norweg)
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])  # Uses 0 by default
print(parrot[10:15])    # need 1 higher than last element
print(parrot[10:])   # Extends to last element by default

print()
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:]) # original string on same line
print(parrot[:])
#print(parrot[]) # can't use blank

# Experimenting
print()
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[1:4])

# Using negative slice indicies
print()
print(parrot[-4:-2])    # (-4,-3) "Bl"
print(parrot[-4:12])    # (-4,-3) or (11,12) "Bl"
print()
print(parrot[0:6])
print(parrot[(0-14):(6 - 14)])
print(parrot[-14:-8]) # it seems negative indicies are rec as positive

