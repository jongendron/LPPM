# create a generator to return fibonacci sequence
def fibonacci():
    """Infinite generator for fibonacci sequence."""
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current
        # yield current


fib = fibonacci()

# for f in fib:  # leads to stack overflow with infinite series
#     print(f)