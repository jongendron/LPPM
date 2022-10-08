import random   # imports random module


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user, until
    a valid `int` is entered.

    :param prompt: The string that the user will see, when they're
        prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True: # loop until valid input
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp) # return causes execution to leave function (will leave while without calling a break)
        # else:
        #     print("'{0}' is not a valid integer".format(temp))
        print("'{0}' is not a valid integer".format(temp)) # else is not necessary


# print(input.__doc__) # return docstring attribute for function input
# print("*" * 80)
# print(get_integer.__doc__) # return docstring attribute for function get_integer
# print("*" * 80)
help(get_integer)

highest = 10
answer = random.randint(1, highest)  # dot notation: module.function
# print(answer)   # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0               # initialized
guesses = 0             # starts with 1 guess

while guess != answer:
    guess = get_integer(": ")
    guesses += 1
    if guess == 0:
        print("Sorry you couldn't guess it.")
        break
    if guess < answer:
        print("Please guess higher.")
    if guess > answer:
        print("Please guess lower.")

if guess == answer:
    print("Well done, you've guessed it in {} tries.".format(guesses))

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
