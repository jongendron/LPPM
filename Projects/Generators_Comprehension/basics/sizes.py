import sys

# Our own version of generator for big_range
def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("\tmy_range is returning {}".format(start))
        # return start  # returns 1 value and stops
        # yield -> returns yielded value -> goes into suspeded state (keeps track of all variables and where in code it is) -> each call it reawakens 
        # it is called each time it is iterates over, not just once (like return)
        yield start
        start += 1


# create a range object (iterator & generator)
big_range = range(5)
# big_range = my_range(5)  # bad to set generator to variable, b/c the pointer location can change after each next() call
# _ = input("line 19")
# print(next(big_range))  # return next value of generator (which is first here) | It "consumes it" for you
print("big_range is {} bytes".format(sys.getsizeof(big_range)))  # static memory usage

# create a list containing all the values in big_range (iterator not generator)
big_list = []
# _ = input("line 25")
for val in big_range:  # calls next in the generator for us
    # _ = input("line 27 - inside loop")
    big_list.append(val)
print("big_list is {} bytes".format(sys.getsizeof(big_list)))  # non-static memory usage (much larger!)

# Print out objects
print(big_range)
print(big_list)

print("\nlooping again ... or not\n")  
for i in big_range:  # nothing prints b/c generator my_range 'pointer' has reached the end of iteration and does not get reset
# for i in my_range(5):  # creates new generator of my_range()
    print("i is {}".format(i))  # does work if you use range() b/c it resets on it's own