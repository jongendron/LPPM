# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:45:38 2022

@author: jonge
"""
# dictionary values are actually memory stored outside of dictionary and the keys
# access the memory location

lion_list = ['scary', 'big', 'cat']
elephant_list = ['big', 'grey', 'wrinkled']
teddy_list = ['cuddly', 'stuffed']

# This is what the structure of a list really looks like
# the keys are linked to other memory (stored as object or just memory space)
animals = {
    'lion': lion_list,
    'elephant': elephant_list,
    'teddy': teddy_list,
    }

#things = animals.copy() # things is now a copy of the dictionary
# This is what the copy actually looks like
things = {
    'lion': lion_list,
    'elephant': elephant_list,
    'teddy': teddy_list,
    }

print(animals['teddy'])
print(things['teddy'])

print()

#things['teddy'].append("toy") # things is a shallow copy, so its values are still links
#print(animals['teddy'])
#print(things['teddy'])

#print()

# but if we change the original list, then it will change dictionary values linked to it
# all are appened here
teddy_list.append('toy') # things is a shallow copy, so its values are still links
animals['teddy'].append('added via `animals`')
things['teddy'].append('added via `things`')
print(animals['teddy'])
print(things['teddy'])
print(teddy_list)
