# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:32:15 2023

@author: jonge
"""

import csv

input_filename = 'country_info.txt'

#%% Specify field separater manually or with sniffer ('|' instead of ',')
with open(input_filename, encoding='utf-8', newline='') as countries_data:
    #sample = countries_data.read() # read entire contents of file as string, therefore pointer is at end
    sample = "" # sample used in sniffer must be in string format and include field separaters and newline characters
    for line in range(3):
        sample += countries_data.readline()
# =============================================================================
#     # also works to generate sample of text for sniffer (3 lines)
#     i = 0
#     for line in countries_data:
#         sample += line
#         i += 1
#         if i > 3:
#             break
# =============================================================================
    countries_data.seek(0) # resets the file point to the start of the file (0)
    country_dialect = csv.Sniffer().sniff(sample) # describes format of data
    country_dialect.skipinitialspace = True # skips whitespace before text in each field check last row of this file
    #country_reader = csv.reader(countries_data, delimiter='|')
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)        
#%% What's in a csv.dialect object
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]

for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')
    
# if you print a string containing line feeds ('\n, \t, \r, ... etc) it prints new lines instead
# use repr() returns a string that shows these escape characters rather their their actions
# it can be used to replace str() 