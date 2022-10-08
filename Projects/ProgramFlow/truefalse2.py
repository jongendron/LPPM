# 0 always evaluates to False
if 0:
    print("True")
else:
    print("False")

# if nothing is input (empty) if -> False; or else string -> True
name = input("Please enter your name: ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

# Same as this (if name does not equal empty string)
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
