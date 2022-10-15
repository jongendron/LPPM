# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:01:31 2022

@author: jonge
"""
#%%
d = {
     0: "zero",
     1: "one",
     2: "two",
     3: "three",
     4: "four",
     5: "five",
     6: "six",
     7: "seven",
     8: "eight",
     9: "nine",
     "iv": "four"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

#%% The `values` method to get values from a dictionary
v = d.values()
print(v)

d[10] = 'ten'
print(v) # and it updates automatically

print("four" in v) # check if value exists in dictionary values
print("elevn" in v) # but doesn't give you the key

# could convert both keys and values to list
# only finds first occurence however
keys = list(d.keys()) 
values = list(v)     # => list(d.values())

if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")
    
print()

# or could loop through to save memory
# finds all occurences though
for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")
 

#%% The `update` method

# Update the dictionary based on another dictionary
# This changes existing elements and/or adds new ones
# Keeps them in the same place
d2 = {
      7: "lucky seven",
      10: "ten",
      3: "this is the new three"
      }

d.update(d2)
for key, value in d.items():
    print(key, value)
    
print()

#Enumerating a list to get an iterable of key value pairs as tuples
# then use them to update the dictionary
d.update(enumerate(pantry_items))
for key, value in d.items():
    print(key, value)

more_items = [(11, 'eleven'), (12, 'twelve')]
d.update(more_items)

for item in d.items():
    print(item)


#%% Keys Method to return dictionary keys
# Class method (dict is class; fromkeys is the method)

# Create an inital dictionary from a list of keys
new_dict = dict.fromkeys(pantry_items, 0) # class method is method for class
print(new_dict)

# creates view of dictionary keys (like a symbolic link that updates automatically)
keys = d.keys()
print(keys)

for item in d.keys(): # this is easy to understand that we are looping over a dictionary
    print(item)
    


