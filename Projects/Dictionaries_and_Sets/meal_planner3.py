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

#%% Item shopping list (blank dictionary to add too)
shoplist = {}
def update_shoplist(Item: str, Quantity: int, Shoplist: dict = shoplist) -> None:
    """
    Adds an item (`Item`) and the required quantiy to buy (`Quantity`) to a 
    shopping list (`Shoplist`). If an item is already on the list, it will auto-
    matically update the item, rather than duplicate.

    Parameters
    ----------
    Item : str
        Name of item to add to list.
    Quantity : int
        Quantity of this item to add to list.
    Shoplist : dict, optional
        Shopping list dictionary to update.

    Returns
    -------
    None

    """
    
    #%% Check if item already in the shopping list or not
# =============================================================================
#     if Item not in Shoplist:
#         Shoplist[Item] = Quantity  # If item not on shopping list then add it
#     else:
#         Shoplist[Item] += Quantity # Otherwise just add the quanity to the item 
# =============================================================================
    Shoplist[Item] = Shoplist.setdefault(Item, 0) + Quantity # return value of dict or default 0
    return None
    


#%% Running the Program (Display Recipes and ask user which ingredients you want to check)
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
                
                # Update your shopping list
                print("Updating your shopping list.")
                update_shoplist(Item=food_item, Quantity=quantity_to_buy)
    print()

# Print your shopping list

while True:
    show_shoplist = input("Would you like to print your shopping list (yes/no)\n:")
    
    if show_shoplist == "yes":
        print('\nShopping List')
        for item, quant in shoplist.items():
            print(f"{item}: {quant}")
        break
    elif show_shoplist == "no":
        break
    
    
    