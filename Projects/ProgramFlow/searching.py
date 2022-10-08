shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

#item_to_find = "spam"
item_to_find = "albatross"
found_at = None     # none is constant used to initialize (NA)

# for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break   # stops loop after item is found

if item_to_find in shopping_list:       # this is more efficient
    found_at = shopping_list.index(item_to_find)

# print("{} found at position {}".format(shopping_list[found_at], found_at))
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))