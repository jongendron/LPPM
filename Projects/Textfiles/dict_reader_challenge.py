# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:53:19 2023

@author: jonge
"""

input_filename = 'country_info.txt'
countries = {} # empty
alph = 'abcdefghijklmnopqrstuvwxyz'

#%% Split each line of the field separated file into a list (each country)
with open(input_filename) as country_file:
    country_file.readline() # iterates the file pointer to next line each time .readline() is called
    for row in country_file:
        # split text using the "|" field separater
        #data = row.split('|') # split string to list
        data = row.strip('\n').split('|') # remove '\n' first
        #print(data)
        country, capital, code, code3, dialing, timezone, currency = data # unpack list(s)
        #print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name' : country,
            'capital' : capital,
            'country_code' : code,
            'cc3' : code3,
            'dialing_code' : dialing,
            'timezone' : timezone,
            'currency' : currency
            }
        #print(country_dict)
        countries[country.casefold()] = country_dict
        #code_lookup[code.casefold()] = country
        countries[code.casefold()] = country_dict

#print(countries)

#%% get country name from user and return the captial by searching the dictionary
while True:
    country = input('\nEnter the name of a country, or enter 1 for list of countries, or enter 0 to exit: ').casefold()
    if country in countries.keys():
        print(f'Country: {countries[country]["name"]}; Capital: {countries[country]["capital"]}')
    elif country == '1':
        #for item in countries.keys():
        #    print(f'{item}, ', end='')
        for letter in alph:
            print(letter)
            for item in list(filter(lambda x: x.startswith(letter), countries)):
                print('\t',item)
            
        print("\n")
    elif country == '0':
        break
    else:
        print("Country doesn't exist or incorrectly typed")

#%%
#print(countries.keys())
#print('a' in countries.keys())
list(filter(lambda x: x.startswith('a'), countries))
#filter(lambda x: x.startswith('a'), countries)

#TODO: find a way to check for existance of dict-key using hash lookup instead of inefficient loop lookup