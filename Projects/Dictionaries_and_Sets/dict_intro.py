# Dictionaries are specified by curley braces "{}"
# Looks similar to a list
# keys are contained in `''` on the left of the `:`
# values are contained in `''` on the right of the `:`
# Indexed keys must match exactly!
# Indexing is faster than get method (crashed program)
# get method returns none if index does not exist, so use when you are unsure
# Note: Sometimes you want your code to crash if value doesn't exist


vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    "can-am": 'Bombardier Can-Am 250',
    'virago': "Yamaha XV250",
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple' # using key again overwrites first entry, put preserves original key position
}

# Using a key to index a dictionary
my_car = vehicles['fiesta'] # key is used to index the value rather than a number to index position
print(my_car)

commuter = vehicles['virago']
print(commuter)

# test1 = vehicles['Fiesta'] # returns error
# print(test1)

# Using get method to get values from a dictionary
learner = vehicles.get("er5") # er5 is indexed and extracted from dictionary
print(learner)

test2 = vehicles.get("Fiesta") # returns None if does not exist

# Note: '' or "" can be used to define the key and the value
print(vehicles["can-am"],vehicles['can-am'],vehicles["virago"],vehicles['virago'])
print()

# Dictionaries are also iterable!
# Iterates over the keys (and values)
for key in vehicles:
    print(key,vehicles[key], sep="; ")
print()

# Adding items to a dictionary
# There is no append method to dictionaries
vehicles["starfighter"] = "Lockheed F-104" # adds "Lockheed F-104" to dict using "startfighter" as key
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"
# vehicles[str(input("Type a key:"))] = str(input("Type a value:")) # if you want to add with input
key_tmp = "mini"
value_tmp = "Mini Cooper"
vehicles[key_tmp] = value_tmp # adding key and value using variables

# Changing values in a dictionary
vehicles["virago"] = "Yamaha XV535" # changes value put preserves key position

# Deleting dictionary items
del vehicles["starfighter"]
# del vehicles["f1"] # trying to remove items that don't exist will crash your program
# vehicles.pop("f1") # if you want an error thrown, but no code crash
vehicles.pop("f1", None) # if you are not sure if item exists and you don't want error or crash
result = vehicles.pop("f1", None) # returns None
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet") # saves the value to variable plane and remove from dictionary
print(plane) # retuns none if key does not exist
bike = vehicles.pop("tenere", "not present") # same, but returns custom default value if output if not present
print(bike)
print()


# Can also "unpack" dictionaries (like enumerate for tupples)
# This is much faster than using indexing on each line
# This is because it uses a "generator"
# The generator does not require python to create a separate list coerced from the dictionary
print(vehicles.items()) # creates a list of tupples; each tupple contains key and value for each dictionary index
print()

for item in vehicles.items(): # iterates over a list of tupples
    print(item)
print()

for key, value in vehicles.items(): # iterates over the list of tupples, also upacks them into variables "key" and "value"
    print(key, value, sep="; ")
print()



