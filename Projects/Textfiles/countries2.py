# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:53:19 2023

@author: jonge
"""

import csv

input_filename = 'country_info.txt'
dialect = csv.excel # use excel dialect template
dialect.delimiter = '|' # change deliminater to pipe
#custom_dialect = csv.Dialect(delimiter='|') # incorrect
countries = {} # empty

# Split each line of the field separated file into a list (each country)
with open(input_filename, 'r', encoding='utf-8', newline='') as country_data:
    # Get the column headings form the first line of the file
    headings = country_data.readline().strip('\n').split(dialect.delimiter)
    headings = [item.casefold().strip(' \t') for item in headings]
    #reader = csv.DictReader(country_data, delimiter='|', skipinitialspace=True)
    reader = csv.DictReader(country_data, dialect=dialect, fieldnames=headings) # manual fieldnames headings
    for row in reader:
        #countries[row['CC'].casefold()] = row
        countries[row['cc'].casefold()] = row
        #countries[row['Country'].casefold()] = row
        countries[row['country'].casefold()] = row
        
#for key, value in countries.items():
#    print(f'{key}: {value}\n')
     
while True:
    choice = input('\nEnter a country name or their CC code: ').casefold()
    if choice in countries:
        country_info = countries[choice]
        #print(f'The capital of {country_info["Country"]} is ... {country_info["Capital"]}')
        print(f'The capital of {country_info["country"]} is ... {country_info["capital"]}')
    elif choice == 'exit' or choice == 'quit':
        break