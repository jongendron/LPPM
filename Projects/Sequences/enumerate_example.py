# Enumerate function extracts indicies and items from a sequence
# for index, character in enumerate("abcdefgh"): # this actually unpacks tuple
#     print(index, character)

for t in enumerate("abcefgh"):
    index, character = t
    print(t) # t is now assigned to tupples
    print(index, character) # unpackes the tuple -> index, and character
    # This is essentially the same as the first loop on this page

# This is what is happening on line 2
# index, character = (0, 'a')
# print(index)
# print(character)
