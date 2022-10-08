flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflowe",
    "Tiger Lily"
]

# Iterate over list and print items
# for flower in flowers:
#     print(flower)

# Join() takes iterable and joins all items in the iterable
# and uses string we called it on as the separator
# also creates string from a list
# !!! All items in iterable must be strings for this to work (not integers)

# separator = " | "
# output = separator.join(flowers)
# print(output) # each flower is joined into single string with "space" "bar" "space"

separator = ", "
output = separator.join(flowers)
print(output) # each flower is joined into single string with "space" "bar" "space"

print(",".join(flowers)) # works the same

# Python lets you store different types of items in a list, but some programs will crash if they are not homogenous
# for example a list of all strings and one integer can't be passed through join

# More on joining

generated_list =['9', ' ',
                 '2', '2', '3', ' ',
                 '3', '7', '2', ' ',
                 '0', '3', '6', ' ',
                 '8', '5', '4', ' ',
                 '7', '7', '5', ' ',
                 '8', '0', '7']
# print(generated_list)
values = "".join(generated_list)
print(values)
values = "".join(generated_list).split()
print(values)
