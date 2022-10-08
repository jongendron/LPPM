even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd) # merges the two lists
print(even)

even.sort()             # sorts the list lowest to highest
print(even)
another_even = even     # links another object to the list
print(another_even)

even.sort(reverse=True) # sorts the list highest to lowerest
print(even)
print(another_even)     # also was altered

# sort() does not create copy of the list (changes existing)
# this prevents extra memory