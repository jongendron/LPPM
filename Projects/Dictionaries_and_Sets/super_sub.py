# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 23:24:09 2023

@author: jonge
"""

animals = {'turtle',
           'horse',
           'robin',
           'python',
           'swollow',
           'hedgehog',
           'wren',
           'aardvark',
           'cat'
           }

birds = {'robin', 'swollow', 'wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')
print(f'birds is a superset of animals: {birds.issuperset(animals)}')

#%% Check using operators
print(birds <= animals) # subset
print(birds < animals)  # proper subset

print('*' * 80)

garden_birds = {'swollow', 'wren', 'robin'}

print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds) # check for proper subset

print('*' * 80)

more_birds = {'wren', 'budgie', 'swollow'}
print(garden_birds >= more_birds)

# Disjoint is when there are no elements in common (see python docs for this)

