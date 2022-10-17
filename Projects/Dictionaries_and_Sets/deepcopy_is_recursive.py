# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 15:45:26 2022

@author: PETBUser
"""

from my_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]]
    }

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original['Tim'].append("Australia")
original['J-P'].append("UK")

# Change second item in list time and J-P in two diff ways
original['Tim'][1].append('Cashier') # directly
jp_list = original['J-P'] # indirectly
jp_list[1].append('Courier')

print(original,'\n')
print(copy_1, '\n')
print(copy_2, '\n') # did not copy recursively