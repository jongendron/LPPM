# Index values can be removed from for loops if iterating backwards
# once an item or slice of items are deleted, the index of all items with indices higher
# shift to close the gap with lower value items that were to the left of the items removed
# in order to preserve ordered sequence of indices

data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
print(data)

min_valid = 100
max_valid = 200

for index in range(len(data) - 1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

print(data)

