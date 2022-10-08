empty_list = [] # list literal (empty list)
even = [2, 3, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd # concatinated two lists into new one
print(numbers)

sorted_numbers = sorted(numbers) # creates new sorted list
print(sorted_numbers)
print(numbers) # this list was not changed

digits = sorted("432985617")
print(digits) # list of strings with single digit

digits2 = list("432985617") # list() is a class initializer
print(digits2) # creates with in same order as input string

# Copying lists to new objects rather than linking new variable to memory
more_numbers = list(numbers) # (list())this creates a new list from numbers
print(more_numbers)
print(numbers is more_numbers) # check to see if they are same list (memory address)
print(numbers == more_numbers) # checks if object have equal values

more_numbers2 = numbers[:] # (slice) also copies all elements of numbers -> new list
print(more_numbers2)
print(numbers is more_numbers2) # check to see if they are same list (memory address)
print(numbers == more_numbers2) # checks if object have equal values

more_numbers3 = numbers.copy() # (copy()) copies the list object (python 3.3)
print(more_numbers3)
print(numbers is more_numbers3) # check to see if they are same list (memory address)
print(numbers == more_numbers3)
