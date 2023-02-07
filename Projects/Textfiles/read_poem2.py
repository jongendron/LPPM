# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 19:42:43 2023

@author: jonge
"""

#%% Python encoding errors can cause strange printouts
# encoding is platform dependent
# specify Jabberwocky.txt is encoded as utf-8 to fix this
# -> default 'windows-1252'
# -> common 'utf-8'
#with open('Jabberwocky.txt', encoding='windows-1252') as jabber:
with open('Jabberwocky.txt', encoding='windows-1252') as jabber: 
    for line in jabber:
        print(line.rstrip())