# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:41:53 2022

@author: PETBUser
"""

from contents import pantry, recipes

# Dictionary comprehension (more efficient code)
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
    # print(index, key) # keys are indexes of dictionary, not index
    display_dict[str(index + 1)] = key
    
while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-"*40)
    for key, value in display_dict.items():
        print(f"{key} - {value}")
        
    choice = input(": ")
    
    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"\nYou have selected {selected_item}, the following ingredients are required ...\n")        
        ingredients = recipes[selected_item]
        print(ingredients,"\n")
        
        # Now check if you have these ingredients in the pantry
        print("Checking if ingredients are available ...\n")
        can_cook = True
        sufficient = []
        insufficient = []
                
        for item in ingredients:
            if item not in pantry:
                #print(f"\tInsufficient: {item}\n")                
                insufficient.append(item)
                can_cook = False
            elif pantry[item] < 1:
                # print(f"\tInsufficient: {item}\n")
                insufficient.append(item)
                can_cook = False         
            else:
                sufficient.append(item)
                
        if can_cook == True:
            print(f"Panty has all ingredients to cook {selected_item}.\n")
        else:
            print(f"Pantry is missing ingredients ...\n\t\tSufficient: {sufficient}\n\t\tInsufficient: {insufficient}\n")
            
            
        
            
        
        
    

