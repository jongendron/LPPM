# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:00:50 2022

@author: jonge
"""

farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'} # {}'s like dict, but not keys
print(farm_animals)
print() # sets are unordered and print randomly

for animal in farm_animals:
    print(animal)
print()

print(type(farm_animals))

#print('Indexing a set is impossible')
#goat = farm_animals[3]
#print(goat)

more_animals = {'sheep', 'goat', 'cow', 'horse', 'hen'}
if more_animals == farm_animals:
    print('Sets are equal')
else:
    print('Sets are different')