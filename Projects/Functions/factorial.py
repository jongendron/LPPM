# (1) save input number
# (2) loop from 1 to that numbe (inclusive)
# (3) multiply by the value in the loop each iteration

def factorial(number: int) -> int:
    """
    Computes the factorial of `number`

    :param number: the number to obtain the factorial for
    :return: Returns the factorial of `number`
    """
    if number == 0:
        return 1
    i = 1
    answer = 1
    while i < (number + 1):
        answer = answer * i
        i += 1
    return answer

print(factorial(5))
