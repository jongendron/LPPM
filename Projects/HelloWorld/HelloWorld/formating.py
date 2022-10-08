# Alignment
# :n shows n spaces with default alignment
# :<n is left align n spaces
# :>n is right align right align n spaces
# :^n is center align center align n spaces

# To right align replacement values
# {0:2} formats replacment 0 with 2 spaces
# {1:3} formats replacement 1 with 3 spaces
# {2:4} formats replacement 2 with 4 spaces
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# To left replacement values
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# To center align replacement values
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

# Precision and class
# 0:2f -> prints 0 with width of 2 as a float
# 0:2.nf --> prints 0 with width of two as a float with prec n
# 0:<2.nf --> prints 0 with width of two left asigned with prec n

print("Pi is approximately {0:<12}".format(22 / 7))      # default
print("Pi is approximately {0:<12f}".format(22 / 7))     # float
print("Pi is approximately {0:<12.50f}".format(22 / 7))  # float w/ precision more important than width
print("Pi is approximately {0:<52.50f}".format(22 / 7))  # float w/ prec 50 and width 52
print("Pi is approximately {0:<72.50f}".format(22 / 7))  # float w/ prec 50 and width 52
print("Pi is approximately {0:<72.54f}".format(22 / 7))

print()

# without proving field number specified it uses the first by default
# and the cycles through the format list in order
# but you can't use a value more than once because no indices specified
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    