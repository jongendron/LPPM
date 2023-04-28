import timeit

n1 = 100  # works


def fact(n=n1):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
 
 
def factorial(n=n1):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# n1 = 100  # doesn't work

if __name__ == "__main__":
    list1 = timeit.timeit("x = fact()", setup="from __main__ import fact", number=1000, repeat=6)
    list2 = timeit.timeit("x = factorial()", setup="from __main__ import factorial", number=1000, repeat=6)
    print(list1)
    print(list2)
    