# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:37:08 2023

@author: jonge
"""

import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']

filename = 'albums.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
# zip function -> trasnforms iterable of X -> iterable containing tuples
    for row in albums:
        #print(row)
        zip_object = zip(keys, row)
        #print(zip_object)
        #for thing in zip(keys, row):
            #print("\t", thing)
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)

#%% but what happens if zip objects contain tuples of 3 elements?
