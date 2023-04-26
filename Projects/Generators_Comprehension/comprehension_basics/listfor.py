print(__file__)

# Non-comprehension (for-loop)
numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number, and I'll tell you it's square: "))

squares = []
for number in numbers:
    squares.append(number ** 2)  # get square root

# Error: number is also loop control variable and overwrite number
index_pos = numbers.index(number)
print(squares[index_pos])
print()