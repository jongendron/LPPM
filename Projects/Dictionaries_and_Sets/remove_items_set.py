# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:31:49 2022

@author: jonge
"""

# initialize a set
small_ints = set(range(21))
print(small_ints)

# clear the set
#small_ints.clear()
#print(small_ints)

# remove
small_ints.discard(10)
small_ints.remove(11)
print(small_ints)
#small_ints.remove(99)
#print(small_ints) # if number is not in set, it will cause a crash

# discard
small_ints.discard(99)
print(small_ints)

# Use remove when you want to be flagged that item is not in a set when removing
