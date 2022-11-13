# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:25:10 2022

@author: jonge
"""

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...
for character in text:
    if character.isalnum():
        word_count[character.lower()] = word_count.setdefault(character.lower(), 0) + 1
 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
