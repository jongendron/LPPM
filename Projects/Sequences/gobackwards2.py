# Index values can be removed from for loops if iterating backwards
# once an item or slice of items are deleted, the index of all items with indices higher
# shift to close the gap with lower value items that were to the left of the items removed
# in order to preserve ordered sequence of indices

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
print(data)

min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

# Reversed function reverses the sequence
# indexes still start from 0 but item zero
# now corresponds to the last item in the list
# and indexes correspond to items from sequence
# as if they were being called right to left

top_index = len(data) - 1 # minus one because last indexes start at zero (not 1)
# for index, value in enumerate(reversed(data)):
#     print(top_index - index, value)

for index, value in enumerate(reversed(data)): # enumerate is more efficient than index lookups
    if value < min_valid or value > max_valid:
        print(top_index - index, value) # this is index position of list if the list was not reversed
        del data[top_index - index]

print(data)

