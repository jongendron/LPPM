# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:50:22 2022

@author: jonge
"""

from prescription_data import *

trial_patients =['Denise', 'Eddie', 'Frank', 'Georgia', 'Kenny']

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # Check if warfarin is in set first before removing (inefficient)
    #if warfarin in prescription: # inefficient | checks all items        
    try: # replaces linear check with exception is more efficient
        prescription.remove(warfarin) # we want error flag to  be thrown
        #prescription.discard(warfarin) # Kenny becomes problem if warfarin not in set
        prescription.add(edoxaban)
    #else:
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin"
              f" Please remove {patient} from the trial")
    print(patient, prescription)