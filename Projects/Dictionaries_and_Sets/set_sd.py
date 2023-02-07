# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 18:34:44 2022

@author: jonge
"""
#symetric difference is opposite of intersection

morning = {'java', 'c', 'ruby', 'lisp', 'c#'}
afternoon = {'python', 'c#', 'java', 'c', 'ruby'}

possible_courses = morning ^ afternoon
print(possible_courses)

morning = ['java', 'c', 'ruby', 'lisp', 'c#']
afternoon = ['python', 'c#', 'java', 'c', 'ruby']

possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

