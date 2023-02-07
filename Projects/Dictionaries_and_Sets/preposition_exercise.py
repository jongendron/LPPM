# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:49:47 2022

@author: jonge
"""

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

words = set(text.split())
preps_used = words & prepositions
print(preps_used)