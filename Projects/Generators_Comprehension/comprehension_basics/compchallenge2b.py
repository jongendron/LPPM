import timeit

setup = """\
gc.enable()  # to enable garbage collection in testing
# Built-in Functions: https://docs.python.org/3/library/functions.html
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # exit to forest
         2: {"N": 5, "Q": 0},  # exit to forest
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""
# Built-in Functions: https://docs.python.org/3/library/functions.html
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # exit to forest
         2: {"N": 5, "Q": 0},  # exit to forest
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

# print("nested for loops")
# print("----------------")
# nested_loop = """\
def nested_loop():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
        # print("Locations leading to {}".format(loc), end='\t')
        # print(exits_to_destination_1)
    # print the result before returning
    # this shows that generators suffer when iterating
    for x in result:
        pass
    return result


# """
print()

# print("List comprehension inside a for loop")
# print("------------------------------------")
# loop_comp = """\
def loop_comp():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        # print("Locations leading to {}".format(loc), end='\t')
        # print(exits_to_destination_2)
        result.append(exits_to_destination_2)
    # print the result before returning
    # this shows that generators suffer when iterating
    for x in result:
        pass
    return result


# """
print()

# print("Nested list comprehension")
# print("--------------------------")
# nested_comp = """\
def nested_comp():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
    # exits_to_destination_3 = [(loc, [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]) for loc in sorted(locations)]
    # for index, loc in enumerate(exits_to_destination_3):  # using index number position to specify location w/ enumerate
    #     print("Locations leading to {}".format(index), end='\t')
    #     print(loc)
    # print the result before returning
    # this shows that generators suffer when iterating
    for x in exits_to_destination_3:
        pass
    return exits_to_destination_3

# """

# creating generator is faster than building list
# we pay for performance when iterating over a generator
def nested_gen():
    exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations))
    # exits_to_destination_3 = [(loc, [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]) for loc in sorted(locations)]
    # for index, loc in enumerate(exits_to_destination_3):  # using index number position to specify location w/ enumerate
    #     print("Locations leading to {}".format(index), end='\t')
    #     print(loc)
    # print the result before returning
    # this shows that generators suffer when iterating
    for x in exits_to_destination_3:
        pass
    return exits_to_destination_3


print(nested_loop())
print(loop_comp())
print(nested_comp())
print(nested_gen())

# timeit.timeit() -> returns process run time (to <times> iterations)
# globals = globals() defines global namespace
# setup = <string of code> defines code that stmt depends on
# result1 = timeit.timeit(nested_loop, globals = globals(), number = 1000)
# Typically avoid printing to screen when testing time because it can significantly influence performance 
# (and can be unstable influence)
# can only test functions that don't use arguements
result1 = timeit.timeit(nested_loop, setup = setup, number = 1000)
result2 = timeit.timeit(loop_comp, setup = setup, number = 1000)
result3 = timeit.timeit(nested_comp, setup = setup, number = 1000)
result4 = timeit.timeit(nested_gen, setup = setup, number = 1000)
print("Nested loop:\t{}".format(result1))
print("Loop comp:\t{}".format(result2))
print("Nested comp:\t{}".format(result3))
print("Nested gen:\t{}".format(result4))