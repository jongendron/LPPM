# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 13:11:06 2023

@author: jonge
"""

import csv

csv_filename = "cereal_grains.csv"

#%% When csv file has quoted strings (not numbers), you flag to convert numbers
# this converts all numeric values to floats (rather than ints)
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC) # non numeric values are quoted
    for row in reader:
        print(row)
    