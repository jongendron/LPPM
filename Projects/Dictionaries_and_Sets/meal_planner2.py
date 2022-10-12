# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:41:53 2022

@author: PETBUser
"""

from contents import pantry, recipes

# Dictionary comprehension (more efficient code)
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}

#%% Creating display dictionary
display_dict = {}
for index, key in enumerate(recipes):
    # print(index, key) # keys are indexes of dictionary, not index
    display_dict[str(index + 1)] = key
 
#%% Displaying Menu Items
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
        print(f"\nYou have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients,'\n')
        # for food_item in ingredients: # loop through dictionary keys
        for food_item, required_quantity in ingredients.items(): # loop through dictionary items
            # if food_item in pantry: # check if food_item is a key in pantry dict
            quantity_in_pantry = pantry.get(food_item, 0) # doesn't crash if item doesn't exist (instead returns 0)
            if required_quantity <= quantity_in_pantry: # check if food_item is a key in pantry dict
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                # print(f"\tYou don't have a necessary ingr1edient: {food_item}")
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
    print()

