# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
from statistics import mean, stdev
 
 
def fact(n=100):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
 
 
def factorial(n=100):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    

# x = fact(130)
# print(x)
# y = factorial(130)
# print(y)

# Test performance of both functions on 100 factorial
# result1 = timeit.timeit(fact, number=1000)
# result2 = timeit.timeit(factorial, number=1000)

# print(f"factorial looping: {result1}")
# print(f"factorial recursion: {result2}")

if __name__ == "__main__":
    # print(timeit.timeit("x = fact(100)", setup="from __main__ import fact", number=1000))
    # print(timeit.timeit("x = factorial(100)", setup="from __main__ import factorial", number=1000))
    
    # repeat timeit.timeit()
    # print(timeit.repeat("x = fact(100)", setup="from __main__ import fact", number=1000, repeat=6))
    # print(timeit.repeat("x = factorial(100)", setup="from __main__ import factorial", number=1000, repeat=6))

    
    list1 = timeit.repeat("x = fact(100)", setup="from __main__ import fact", number=1000, repeat=6)
    list2 = timeit.repeat("x = factorial(100)", setup="from __main__ import factorial", number=1000, repeat=6)
    
    # sum of repeats
    # print(sum(list1))
    # print(sum(list2))

    # Getting mean, stdv
    # only useful if you cant account for all variables
    # so many other factors effecting timeing on multi-tasking OS
    # therefore mean and stdev are practically meaningless here
    print(mean(list1), stdev(list1))
    print(mean(list2), stdev(list2))