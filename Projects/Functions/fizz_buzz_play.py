# If a number is divisible by 15, then it is divisible by 3 & 5
# any number divisible by the product of two numbers is divisible
# by those two numbers

def fizz_buzz(number: int) -> str:
    """
    Prints "fizz", "buzz", or "fizz buzz" based on value of integer `number`.

    "fizz" is returned when number is divisible by 3.

    "buzz" is returned when the number is divisible by 5.

    "fizz buzz" is returned when the number is divisible by both 3 and 5.

    "error" is returned when the number does not pass any of these tests (impossible)

    :param number: The number to be assessed.
    :return: Returns either the value of `number`, "fizz", "buzz", "fizz buzz", or "error".
    """
    if (number % 3) != 0 and (number % 5) != 0:
        # print(number)
        return number.__str__()  # coerce int to string
    elif (number % 3) == 0 and (number % 5) == 0:
        # print("fizz buzz")
        return "fizz buzz"
    elif (number % 3) == 0:
        # print("fizz")
        return "fizz"
    elif (number % 5) == 0:
        # print("buzz")
        return "buzz"
    else:
        # print("error")
        return "error"

# print(fizz_buzz("nope")) # throws error
# print(fizz_buzz(-3)) # negatives work

LOW = 1
HIGH = 100
next = LOW + 1
score = 0 # count score
answer = LOW
guess = input("""Let's play Fizz Buzz! Starting with {0}, guess...
\t(1) `fizz` if {0} + 1 is divisible by 3
\t(2) `buzz` if {0} + 1 is divisible by 5
\t(3) `fizz buzz` if {0} + 1 is divisible by 3 & 5 (15)
\t(4) `{1}` if {0} + 1 is not divisible by 3 or 5
""".format(LOW,next))
guess = str(guess)

for i in range(LOW + 1,HIGH + 1):
    answer = fizz_buzz(i)
    next += 1
    if guess != answer:
        print("Sorry, the answer is {0}. You scored {1}"
              .format(answer,score))
        break
    score += 1
    guess = input("Correct, {0} is the answer. Now guess the value of {1} + 1.\n"
                  .format(answer,i))

# Goal: player guesses the fizz_buzz game response
# as the computer iterates from `LOW` to `HIGH`

# Rule: If the player guesses correct, they gain a point and move
# to the next round, but if they guess incorrect then the game ends

# Method: Starting with LOW, the player guesses whether the computer
# will return either ...
# (a) that number if it is not divisible by 3 or 5
# (b) "fizz" if it is divisible by 3
# (c) "buzz" if it is divisible by 5
# (d) "fizz buzz" if it is divisible by 15 (both 3 and 5)
# once the player makes a mistake, the game ends and their
# score will print to the screen
