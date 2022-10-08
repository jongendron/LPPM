pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram) # returns list in alphabetical order
print(letters)

numbers = [2.3,4.5,8.7,3.1,9.2,1.6]
#sorted = sorted_numbers(numbers) # can't name variable same as built-in name
sorted_numbers = sorted(numbers)
print(sorted_numbers)   # creates new sorted list
print(numbers)          # original list preserved

# another_sorted_numbers = numbers.sort()          # sorts in place (new list not created)
# print(numbers)
# print(another_sorted_numbers) # sorted() returns None
numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold) # sort case insensitive
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort()
print(names)

names.sort(key=str.casefold)
print(names)
