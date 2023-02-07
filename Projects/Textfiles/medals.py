# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 22:40:52 2023

@author: jonge
"""

import csv

#%%
csv_filename = 'OlympicMedals_2020.csv'
# define newline='' (empty string) to ensure csv.reader() receives newline characters correctly
# newline='' prevents open() from translating newline characters to the csv.reader()
# instead this means csv.read() will do its own translation of the text 
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',') # file pointer moved to line 2 (skips header)
    print(f'Column headers: {headers}')
    #reader = csv.reader(csv_file) # reader object saved; iterable
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row) # causes issue when strings are not quoted!
# =============================================================================
#     for row in reader:
#         #print(row) # each row is a list; each element is a field
#         # convert Rank and Country:Total to ints
#         l = []
#         for i in range(len(row)):
#             if i != 1:
#                 l.append(int(row[i]))
#             else:
#                 l.append(str(row[i]))
#         print(l)
# =============================================================================
        