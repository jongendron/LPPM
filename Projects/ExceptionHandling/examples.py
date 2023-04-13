# Two types of errors: 1. syntax errors and 2. exceptions.
# Types: https://docs.python.org/3/library/exceptions.html
# Exception handelings are useful for preventing code from crashing, and allow program to recover from error, and even retry different approaches!

# Syntax errors
# x = 8 = 5 # error
x = 8 - 5 # correct

# Exceptions (unexcepted behavior)
# (ex) creating a directory or memory space when your out of disc space
# (ex) zero division error
# -> ZeroDivisionError: division by zero
# -> exception: additional information
# Unhandeled exceptions causes program to crash

# example, recursion error (causes stack overflow)
def factorial(n):
    # n! can also be defined as n * (n-1)!
    """calculate n! recursively"""
    if n <= 1:
        return 1
    else:
        # print(n / 0) # to raise /0 exception
        return n * factorial(n-1)
    
# print(factorial(9000)) # causes RecursionError, that makes system run out of memory / overflow the stack.

# Handle the exception with a "try block"
# can stack except clauses in the try block 
try:
    print(factorial(900)) # execute this code and see if error exception is thrown
except RecursionError: # exception handler: the exception error(s) that will be handeled by the program (all other errors will cause program to crash)
    print("This program cannot calculate factorials that large because they cause stack overflow!") # code to run if the exception is raised
except ZeroDivisionError: # can stack except clauses in the try block
    print("What are you doing dividing by zero?")

# Alternatively you can handel more than one exception/error in a single except clause by using a tuple (or list) of exceptions/errors
try:
    print(factorial(9000)) # execute this code and see if error exception is thrown
#except (RecursionError, ZeroDivisionError): # This method does not make it clear which error was raised though
except (RecursionError, OverflowError): # This does make sense because both errors are due to stackoverflow (they are similar errors with similar causes)
    #print("This program cannot calculate factorials that are too large, nor can you divide by zero!") # code to run if the exception is raised    
    # Data too large to store in computers memory causes "Overflow" (aka stack overflow)
    # you can overflow individual variables by using numbers that are too large --> arithmatic returns values too large for your memory --> OverflowError
    # However, Python handels large numbers very easily
    print("This program cannot calculate factorials that are this large!")

print("Program terminating")

