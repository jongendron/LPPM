# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:17:30 2022

@author: jonge
"""

numbers = {} # does not initialize a set, but rather a dict
print(f"numbers: {type(numbers)}")

numbers = {*""} # you can init an empty set by unpacking an empty object (string, dict, etc)
numbers = set() # easiest way
print(numbers)

# To add values to set
#numbers.add(1)
#print(numbers)

#while len(numbers) < 4:
#    next_value = int(input("Please enter your next value: "))
#    numbers.add(next_value)
#print(numbers)

# Removes duplicates real time and won't stop until you enter 4 uniques

# use survey data
data = ['blue', 'red', 'blue', 'green', 'red', 'blue', 'white'] # ex

# Create a set from a list to remove duplicates
unique_data = set(data)
unique_data = sorted(set(data)) # sort by name
print(unique_data)

# Create a list of unique colors, keeping the order they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)

