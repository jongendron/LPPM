# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:30:07 2022

@author: jonge
"""

from prescription_data import patients

trial_patients = {'Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny'}


# Removes random item from set and returns its value
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end= " : ")
    prescription = patients[patient]
    print(prescription)

print()    
print(trial_patients)
    