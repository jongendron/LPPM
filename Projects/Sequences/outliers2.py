###################################################################
### Removing Outlier values for ordered sequences (low -> high) ###
###################################################################
# data = [4,5,104,105,110,120,130,130,
#         150,160,170,183,185,187,188,191,350,360] # both positive and negative outliers
# data = [4,5,104,105,110,120,130,130,
#         150,160,170,183,185,187,188,191] # only negative outliers
# data = [104,105,110,120,130,130,
#          150,160,170,183,185,187,188,191,350,360] # only positive outliers
# data = sorted([75,1,6,50,1000,5000,6000,900,750,10000]) # no values in raenge
data = []
print(data)

# set min and max values of list
min_valid = 100
max_valid = 200

# Process the low values of a list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
# print(stop) # for debugging
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
# print(start) # for debugging
del data[start:]
print(data)





