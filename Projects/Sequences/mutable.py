shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))                # same id
print(id(another_list))                 # as this

# to concatinate "cookies" to list
shopping_list += ["cookies"]            # cookies must be in brackets
# shopping_list += "cookies"            # each letter in string "cookie" will concatinate
print(shopping_list)
print(id(shopping_list))                # id remains the same because mutable
print(another_list)                     # another_list also points to same object (memory bank)

a = b = c = d = e = f = another_list    # chain assignment | more items bound to item
print(a)
print("Adding cream")
b.append("cream")                       # appends the list and all variables attached
print(c)
print(d)
