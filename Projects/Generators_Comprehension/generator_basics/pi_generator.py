# create generator to return an infinite sequence of odd numbers, starting at 1
def oddnum():
    n = 1
    while True:
        yield n
        n += 2


def pi_series():
    odds = oddnum()  # creates odd number generator
    approximation = 0
    while True:  # infinite loop alternating +/- 4/<odd_number>
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


if __name__ == "__main__":
    
    # Test: print the first 100 numbers to check
    # odds = oddnum()
    # for i in range(100):
    #     print(next(odds))

    # Test: pi approximation
    approx_pi = pi_series()

    for x in range(100000):
        print(next(approx_pi))
