# Factorial Function 1
def fact(n):
    """ Calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


# Factorial Function with recursion
def factorial(n):
    # n! can be defined as n * (n-1)!
    """ Calculate n! with recursion"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    

# Fibinaci Sequence w/ recursion
def fib(n):
    """ F(n) = F(n - 1) + F(n - 2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


# Fibinaci w/ iteration
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result
# Test
for i in range(36):
    #print(i, ": ", fact(i))
    #print(i, ": ", factorial(i))
    #print(i, ": ", fib(i))
    print(i, ": ", fibonacci(i)) # must faster

