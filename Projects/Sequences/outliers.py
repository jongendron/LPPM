###################################################################
### Removing Outlier values for ordered sequences (low -> high) ###
###################################################################

data = [4,5,104,105,110,120,130,130,
        150,160,170,183,185,187,188,191,350,360]
print(data)

# remove a slice of list
# del data[0:2]
# #print(data)
# del data[16:] # the item position changed from previous deletion
# print(data)

# use test to del part of list
min_valid = 100
max_valid = 200

## Changing size of object you are iterating over causes issues!
## This wont work because every time you delete it changes true indicies
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

# Process the low values of a list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) # for debugging
del data[:stop] # up-to but not including
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    # We have the index of the last item to keep.
    # Set 'start' to the position of the first
    # item to delete, which is 1 after 'index'.
    if data[index] <= max_valid:
        start = index + 1 # identity location of first item to delete(14 not 13)
        break
print(start)
del data[start:]
print(data)





