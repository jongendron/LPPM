empty_list = [] # list literal (empty list)
even = [2, 3, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd] # list of lists
print(numbers)

for number_list in numbers:
    print(number_list) # print entire nestest list

    for value in number_list:
        print(value) # print items of nestest list