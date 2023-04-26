print(__file__)

numbers = [1, 2, 3, 4, 5 , 6]

number = int(input("Please enter a number, and I'll tell you it's square: "))

# Using list comprehension
squares = [number ** 2 for number in numbers]  # list comprehension is b/w []'s {} -> set
# squares = [number ** 2 for number in range(1, 7)]

# No Error: number variable is not overwritten by list comprehension
print(squares)
index_pos = numbers.index(number)
print(squares[index_pos])
print()