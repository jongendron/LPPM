# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:26:54 2022

@author: jonge
"""

from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0) # adds new items to dict with default if doesn't exist
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0) # doesn't add new itemd to dict
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight")
print(f"zucchini {z_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
    