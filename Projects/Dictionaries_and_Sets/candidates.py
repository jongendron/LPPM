# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 23:31:56 2023

@author: jonge
"""

required_skills = {'python', 'github', 'linux'}

candidates = {
    'anna' : {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob' : {'github', 'linux', 'python'},
    'carol' : {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel' : {'pascal', 'java', 'c++', 'github'},
    'ekani' : {'html', 'css', 'github', 'python', 'linux'},
    'fenna' : {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'}
    }

#%% Check for candidates that have all skills looking for
interviewees = set()
for candidate, skills in candidates.items():
    #if skills.issuperset(required_skills):
    if skills > required_skills: # check that candidates have more than required skills
        interviewees.add(candidate)
        
print(interviewees)

