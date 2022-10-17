# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 21:16:28 2022

@author: jonge
"""

data = [
        ("orange", "a sweet, orange, citrus fruit"),
        ("apple", "good for making cider"),
        ("lemon", "a sour, yellow citrus fruit"),
        ("grape", "a small, sweet fruit growing in bunches"),
        ("melon", "sweet and juicy")
        ]

# Every letter is actually represented by a number
# ASCII used to be standard
# Now unicode is the standard
# print(ord("a"))
# print(ord("b"))
# print(ord("z"))

#%% Simple Hash Function

def simple_hash(s: str) -> int:
    """
    Rediculously simple hashing function

    Parameters
    ----------
    s : str
        DESCRIPTION.

    Returns
    -------
    int
        DESCRIPTION.

    """
    basic_hash = ord(s[0]) # get ordinal value of first character of string
    return basic_hash % 10

#%% Test the function
for key, value in data:
    h = simple_hash(key)
    print(key, h)

#%% Built-in Hash function
# You can get different hashes each time you run the program
for key, value in data:
    #h = simple_hash(key)
    h = hash(key)
    print(key, h)
    
#%% Creating hash library
keys = [""] * 10 # initialize list of 10 items of empty strings
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    # h = hash(key)
    print(key, h)
    
    keys[h] = key
    values[h] = value

print()
print(keys)
print()
print(values)

# Typically empty strings are not stored in dictionaries (bash libraries)
# But this is just a siplified version
