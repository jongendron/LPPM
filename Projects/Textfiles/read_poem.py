# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 09:46:20 2023

@author: jonge
"""

# Default open() mode is 'r' or read
jabber = open('Jabberwocky.txt', 'r') # open a text file ('r' = read only)

# =============================================================================
# for line in jabber:
#     #print(line, end='') # when new '\n' seen it adds new line
#     print(line.strip(), end='') # removes whitespace from start and end of strings (lines)
#     #print(line.strip()) # add new line between each line printed
#     #print(line.rstrip()) # strip only right right
#     
#     print(len(line))
#     
# jabber.close()

# File handels used by OS to keep track of files that are opened
# Unclosed files may lose data by means of `Resource Leaks`
# =============================================================================

#%% Using Python `with` will close for you
# File closes automatically when 'with' chunk ends

# =============================================================================
# with open('Jabberwocky.txt', 'r') as jabber:
#     # saving individual lines to temporary object
#     for line in jabber:
#         print(line.rstrip())
#     
#     # reading all lines to single object with readlines()
#     # only works for files that can fit into RAM
#     lines = jabber.readlines() # returns list of lines
# 
# print(lines)
# print(lines[-1:]) # print last line
# for line in reversed(lines):
#     print(line, end='')
# 
# =============================================================================

# using readline() moves the file pointer up a level to the next line
# must use file.seek() to reset the file point if you want the same
# line to be extracted from a subsequent readline() call
with open('Jabberwocky.txt') as jabber:
    while True: # every time readline() is called it iterates to next line where as readlines() saves all to list
        line = jabber.readline().rstrip() # saves to an object after stripped
        print(line)
        if 'jubjub' in line.casefold(): # break loop when 'jubjub' found
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip()) # only prints stripped line
        if 'jubjub' in line.casefold():
            break

#%% Reading file with read()
# save text as single string rather than list of lines (strings)
with open('Jabberwocky.txt', 'r') as jabber:
    text = jabber.read()    
#print(text)
for character in reversed(text):
    print(character, end='')
