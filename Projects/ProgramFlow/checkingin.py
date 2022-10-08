parrot = "Norwegian Blue"

letter = input("Enter a character: ")

# check if single character or entire string is in a sequence
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
