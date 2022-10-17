# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:21:17 2022

@author: PETBUser
"""

import copy

#%% Testing 
animals = {
    'lion': ['scary', 'big', 'cat'],
    'elephant': ['big', 'grey', 'wrinkled'],
    'teddy': ['cuddly', 'stuffed'],
    }

# Performa a shallow copy
# things = animals.copy()

# Perform a deep copy
things = copy.deepcopy(animals)

# Compare memory id and list content
print(f"things: {id(things['teddy'])} {things['teddy']}")
print(f"animals: {id(animals['teddy'])} {animals['teddy']}")

print()

# Compare memory id and list content
things['teddy'].append('toy')
print(f"things: {id(things['teddy'])} {things['teddy']}")
print(f"animals: {id(animals['teddy'])} {animals['teddy']}")
