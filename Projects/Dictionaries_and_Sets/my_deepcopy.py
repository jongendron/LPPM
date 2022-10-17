# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:43:10 2022

@author: PETBUser
"""

#%% Function to deep copy

def my_deepcopy(d: dict) -> dict:
    """
    Copy all contentes of a dictionary to new memory. Creates copy of dictionary
    elements that are both `list` and `dict`.
    
    The function will crash with an AttributeError if the values aren't lists
    or dictionaries.
    
    Only copies the first level dictionary elements (if more than 1 nested level)
    the data is not copied to new memory.

    Parameters
    ----------
    d : dict
        The dictionary to copy.

    Returns
    -------
    dict
        A copy of `d`, with values being copies of teh original.

    """
    
    d2 = {}
    
    for key in d:
        #d2[key] = d[key].copy
        d2[key] = d[key].copy()
    
    return d2

#%% Test function

from contents import recipes

recipes_copy = my_deepcopy(recipes)
print(f"recipes_copy: {id(recipes_copy)} {recipes_copy}")
print(f"recipes: {id(recipes)} {recipes}")

print()

recipes_copy['Butter chicken']['ginger'] = 300
print(f"recipes_copy: {id(recipes_copy['Butter chicken']['ginger'])} {recipes_copy['Butter chicken']['ginger']}")
print(f"recipes: {id(recipes['Butter chicken']['ginger'])} {recipes['Butter chicken']['ginger']}")