# --------------------------------------
# Very little need for functools.reduce()
# --------------------------------------

import timeit
import functools


def calc_values(x, y: int):
    return x * y


numbers = [2, 3, 5, 8, 13]

# Using functools.reduce() -> to perform operations
reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)
# print(sum(numbers))  # results in the same

# How it works?
# 1. calls calc_values() with first 2 items in the iteratble numbers (2) and (3)
# 2. calls calc_values() with the result of step 1.
# 3. repeat steps 1 & 2 until iterated through entire list

# This is what it looks like
result = calc_values(2, 3)
result = calc_values(result, 5)
result = calc_values(result, 8)
result = calc_values(result, 13)
print(result)

# So is this ...
result = 1
for x in numbers:
    result *= x
print(result)

# In summary, limit your use of reduce because their is likely a better method