# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 11:45:57 2023

@author: jonge
"""

#%% stripping
filename = 'Jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()
    
print(f'Original: {first}')

# Providing a string to use in strip() 
# doesn't remove only the string passed as arguement
# it takes all characters in string and 
# removes all characters until a non matching character is found
# no need for duplicate characters
chars = "' Twasebv " # strips all these characters from the begginging and end and continues until a non characte match is met
no_apostrophe = first.strip(chars)
print(f'Stripped: {no_apostrophe}')

#%% Manually strip the front of the string (behavior of lstrip)
print(f'Original: {first}')
for character in first:
    if character in chars:
        print(f'removing "{character}" from front of first')
    else:
        break

print("*" * 80)

#%% Manually strip the end of the string (behavior of rstrip)
print(f'Original: {first}')
for character in first[::-1]:
    if character in chars:
        print(f'removing "{character}" from end of first')
    else:
        break
    
print('*'*80)

#%% removing entire string from start or end of string

# =============================================================================
# # removeprefix and removesuffix are Python 3.9 or later
# twas_removed = first.removeprefix("'Twas")
# print(twas_removed)
# toves_removed = first.removesuffix('toves')
# print(toves_removed)
# =============================================================================

#%% Manual functions of removesuffix and remove prefix
def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:] # Return copy of 'string'
    
def removesuffix(string: str, suffix: str) -> str:
    #if string.endswith(suffix): # suffix='' should not all string[:-0]
    if suffix and string.endswith(suffix): # suffix='' should not all string[:-0]    
        return string[:-len(suffix)]
    else:
        return string[:]
    
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
toves_removed = removesuffix(first, 'toves')
print(toves_removed)