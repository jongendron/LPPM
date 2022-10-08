menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"], # redundant common identifies row (use alt + shift + up) to move
]

# Prints all nested lists with spam items removed (Method 1) (works backwards)
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#     else:
#         topid = len(meal) - 1
#         for index, item in enumerate(reversed(meal)):
#             if item == "spam":
#                 del meal[topid - index]
#         print(meal)
#
# print()

# Print all nested lists with spam items removed (Method 2) (works backwards)
# for meal in menu:
#     for index in range(len(meal) -1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)
#
# print()

# Print all nested list with spam items removed (Method 3) (forwards with new list)

# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
#     else:
#         meal2 = []
#         for item in meal:
#             if item != "spam":
#                 meal2.append(item)
#         print(meal2)
#
# print()

# Print only items that are not spam (forwards)
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print()

# Print only items that are not spam (forwards), but keeps items on same line
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item,end=' ') # end with prevent a line break after each item printed
    print()
