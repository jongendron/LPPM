# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 20:19:53 2023

@author: jonge
"""

import json

# =============================================================================
# languages = [
#     ['ABC', 1987],
#     ['Algol 68', 1968],
#     ['APL', 1962],
#     ['C', 1973],
#     ['Haskell', 1990],
#     ['Lisp', 1958],
#     ['Modula-2', 1977],
#     ['Perl', 1987],
# ]
# =============================================================================

# Does not support tupples, only lists -> so will write nested tuples as lists
languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

#%% Serialize data to json format and write to file
with open('test.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

#%% Open jsom format file by deserializing (convert back to nested list)
with open('test.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile) # loaded as nested list
    print(data)
print(data[2]) # print second element of list from deseria
