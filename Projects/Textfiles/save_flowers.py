# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:48:52 2023

@author: jonge
"""
# open(..., 'w') will overwrite previous file if it exists, not append

#%% gather plants data and save to a list
plants_filename = 'plants.txt'
plants = []
with open(plants_filename, 'r') as file:
    file.readline() # skip first line
    for line in file:        
        #print(line.rstrip('\n'))
        line_stripped = line.strip('\n\t ,"][') 
        if line_stripped != '':
            plants.append(line_stripped)

#print(plants)
for plant in plants:
    print(plant)       

#%% write to flowers
flowers_filename = "flowers.txt"

# Default format
with open(flowers_filename, "w") as file:
    for plant in plants:
        print(plant, file=file) # directs standard output stream to plants file


#%% write as csv
with open(flowers_filename, "w") as file:
    for item in plants:
        plant, typ = item.split('-')
        plant = plant.strip(' -')
        typ = typ.strip(' -')
        print(plant, typ, sep=', ', file=file)

#%% Read the flowers from file again
new_list = []

with open(flowers_filename) as file:
    for plant in file:
        new_list.append(plant.rstrip())

print(new_list)

#%% using .write() method
# doesn't have various conversions like print; almost verbatum
flowers_filename = "flowers_write.txt"

with open(flowers_filename, "w") as file:
    for plant in plants:
        file.write(plant) # write to file using .write() method
        
#%% __str__ representation
#print(plants)
string_representation = plants.__str__() # string
print(type(string_representation))

#%% test writing numbers to text file
filename = "test_numbers.txt"
with open(filename, "w") as file:
    for i in range(10):
        print(i, file=file) # obtained string representation of the numbers to write
        
with open(filename, "w") as file:
    for i in range(10):
        #file.write(i) # Error: arguement must be a str, not int
        #file.write(str(i)) # no separators or ends
        file.write(str(i) + '\n')
        
# print() prints the string representation of any object you ask
# -> it also adds a separator between multiple arguements
# -> also adds the character defined in the end keyword arguement
# -> .write() does not do any of these things, and therefore objects
# -> not of class string must be manually converted before being written

# .write() method only writes exactly what you tell it to write
# -> no separators or end characters are included
# -> no conversions are performed, it will write verbatim
# -> if file is opened in text mode, then you get error when you
# --> write things that are not text (i.e. numbers will not work unless converted)
