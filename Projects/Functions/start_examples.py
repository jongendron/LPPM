# How to take 0 ore more arguments into a function and pack them into a tupple

numbers = (0,1,2,3,4,5) # tupple

# print(numbers, sep=";")
# print(*numbers, sep=";") # unpacks the object
# print(0, 1 ,2, 3, 4, 5, sep=";") # same as the unpacked object
# print(numbers, *numbers, sep=";") # see that the packed tupple is on left of ";"


def test_start(*args):
    print(args) # args is a packed tupple of 0 or more input arguments
    for x in args:
        print(x)


# def test_start2(*args, arg2):
#     print("args:", args) # args is a packed tupple of 0 or more input arguments
#     print("arg2:", arg2)
#     for x in args:
#         print(x)

# test_start2(0,1,2,3, arg2="hello")

# test_start(0,1,2,3,4,5) # input arguments are packed into tupple args; there we can have variable # args
# print()
# test_start()  # returns empty tupple

