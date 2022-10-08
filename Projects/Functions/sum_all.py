# Goal: calc the sum of all numbers passed as arguments
# Requirements:
# name: sum_numbers
# needs docstring

# instructions
# sum all numbers passed as arguments of function
# return the sum

def sum_numbers(*numbers: float) -> float:
    """
    Sums all numbers passed as arguments in the function.

    *Function only takes var-positional arguments

    :param numbers: (var-positional arguments) tupple of all arguments passed that will be summed
    :return: sum of all arguments passed
    """
    print("numbers:...{}".format(numbers))
    return float(sum(numbers))

print(sum_numbers(1.2,2.3,3.5))