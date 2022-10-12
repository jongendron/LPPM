# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:24:40 2022

@author: jonge
"""

#%% recipes as nested tuple
recipes_tuple = {
    "Chicken and chips": [
        ("chicken", 100),
        ("potatoes", 3),
        ("salt", 1),
        ("malt vinegar", 5),
        ],
    }
#%% recipes as nested dictionary
recipes_dict = {
    "Chicken and chips": {
        "chicken": 100,
        "potatoes": 3,
        "salt": 1,
        "malt vinegar": 5,
        },
    }
#%% Using tuples
for recipe, ingredients in recipes_tuple.items():
    print(f"Ingredients for {recipe}")
    for ingredients, quantity in ingredients: # ingredients in a tuple
        print(ingredients, quantity, sep=', ')

print()        
#%% Using dictionary
for recipe, ingredients in recipes_dict.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients.items(): # ingredients is a dict
        print(ingredient, quantity, sep=', ')

print()

#%% Test
for item in recipes_tuple.items():
    print(f"Tuple: {item}")
    for tup in item:
        print(f"Tuple item: {tup}")

print()

for item in recipes_dict.items():
    print(item)
    # print(item[1])
    for it in item[1].items():
        print(it)
print()