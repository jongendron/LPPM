# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:49:06 2023

@author: jonge
"""

import csv

cereals_filename = 'cereal_grains.csv'

# reads csv file with a header and covert to dictionary
with open(cereals_filename, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)