# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:45:38 2022

@author: jonge
"""

animals = {
    'lion': ['scary', 'big', 'cat'],
    'elephant': ['big', 'grey', 'wrinkled'],
    'teddy': ['cuddly', 'stuffed'],
    }

#things = animals # things is linked to animals dictionary
#animals['teddy'] = 'toy' # the value of teddy is changed in both `animals` and `things`
#print(animals['teddy'])
#print(things['teddy'])

things = animals.copy() # things is now a copy of the dictionary
#animals['teddy'] = 'toy' # the value of teddy is changed in both `animals` and `things`
print(animals['teddy'])
print(things['teddy'])

print()

things['teddy'].append("toy") # things is a shallow copy, so its values are still links
print(animals['teddy'])
print(things['teddy'])
