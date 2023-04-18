#from __future__ import print_function # import function from new python
# *args allows variable number of arguements (unpacks the tuple)
# -> Doesn't mean you need to pass a tuple as arguement
# -> Does mean that all arguements passed before the first keyword arguement are 
# -> compiled into a tuple, and then unpacked by the function!

#print("Hello", "planet", "earth") # standard print function

# def average(args): # if args is tuple itself, not multiple arguements that are packed into a tuple -> then unpacked
# def average(first_value, *args, last_value) # fails because *args can't be followed by positional arguements (only kewwords)
# def average(first_value, *args): # this does work, but first positional arguement is not part of *args tuple
def average(*args): # *<parameter_name> specifies that all positional arguements until the next keyword arguement will be packed into tuple
    print(type(args))
    print("args is {}:".format(args)) # args is the tuple
    print("*args is:", *args) # *args is the unpacked tuple
    mean = 0
    for arg in args:
        mean += arg
        #print("arg: {}".format(arg))
        #print("mean: {}".format(mean))
    return mean / len(args)

#print(average(1, 2, 3, 4))

# build_tuple: function to take variable number of arguments and return a tuple containing the values passed to it
def build_tuple(*args) -> tuple:
    return args

# message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)

# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)

# Challenges

# 1. function that takes a variable number of words, and returns teh average word length.
def avg_word_len(*args: str) -> float:
    total_len = 0
    for arg in args:
        total_len += len(arg)
    return total_len / len(args)

#val = avg_word_len("hello", "to", "candy")
#print(val)

# 2. funciton that returns the smallest or largest of the numbers passed to it.
def get_bound(*args: float | int, maximum: bool = True) -> float | int:
    """ Get the min/max of the input variables"""
    bound = None
    i = 0
    while True:
        if i > len(args) - 1:
            break
        elif isinstance(args[i], int) or isinstance(args[i], float):
            bound = args[i]
            break
        
            break
        i += 1

    if bound is None:
        raise TypeError("No input arguements were numeric.")

    for arg in args:
        try:
            if maximum and arg > bound:
                    bound = arg
            elif maximum is not True and arg < bound:
                bound = arg
        #except Exception as error:
        except TypeError:
            print("TypeError: '{}' is not an int or float".format(arg))
            #pass
    return bound

#val = get_bound("true", "False", 1.0)
#print("{} is max".format(val))

# 3. function to print all the words passed to it backward, in reverse order.
def rev_str(*args: str) -> None:
    """Print all words entered in reverse."""
    rev = []
    for arg in args:
        try:
            if not isinstance(arg, str):
                raise TypeError("TypeError: {} is not a str.".format(arg))
            #print(arg[::-1], end=" ")
            rev.append(arg[::-1])
        except TypeError as _e:
            print(_e)

    print(*rev)

    return None

#rev_str("One", 1, "three")
#rev_str("Hannah", "is", "hannaH")


# 4. function to print a list, but also print the unpacked list
def list_unpack(*args):
    """Print list and unpacked list"""
    l = list(args)
    print(l)
    print(*l)
    return None

list_unpack(1, "two", 3.0)