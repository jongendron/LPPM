# How to define a function in Python
# def <function_name>(argument1, argument2, ...):
# instructions ...

# def multiply():
#     result = 10.5 * 4
#     return result
#
#
# # Convention is to have 2 blank lines after a function definition
# answer = multiply()  # call the function
# print(answer)  # print the answer


# Using Parameters (placeholders for function to use within)
# arguments are values used by the parameters (parameters take on these values)'
# this is called passing arguments
def multiply2(x, y):
    result = x * y
    return result


# answer = multipy2() # if no default arguments are provided it fails
answer = multiply2(10.5,4)
print(answer)

forty_two = multiply2(6,7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply2(2, val)
    print(two_times)






