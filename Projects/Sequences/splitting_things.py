# Split a string up into words use them to populate a list
# splitting a string will produce a string

# panagram = "The quick brown fox jumps over the lazy dog"
panagram = """The quick brown
fox jumps\tover
the lazy dog"""
words = panagram.split() # default is split by white spaces (tabs, new line, and space) (any number between words)
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(",")) # split by commas -> list

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']

values = "".join(generated_list) # join values separated by "" (no char)
print(values)

values_list = values.split() # split by " " (white spaces) -> list
print(values_list)

# Challenge:
# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints

# Method 1: change in place
# print()
# for idx, value in enumerate(values_list):
#      print(values_list[idx] == value,end=" ")
#      values_list[idx] = int(value)
# print()
# print(values_list)

# Method 2: change in place
# print()
# for idx in range(len(values_list)): # default start is 0 and step is +1
#     # print(idx)
#     values_list[idx] = int(values_list[idx])
# print(values_list)

# Method 3: new list
# print()
# values_list2 = []
# for value in values_list:
#     values_list2.append(int(value))
# print(values_list2)
