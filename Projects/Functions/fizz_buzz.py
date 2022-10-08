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


LOW = 1
HIGH = 1000
count = [0,0,0,0,0] # counts for: number, fizz, buzz, fizzbuzz, and error
answer = "null"

for i in range(LOW,HIGH + 1):
    print(i)
    answer = fizz_buzz(i)

    if answer == "fizz":
        count[1] += 1
    elif answer == "buzz":
        count[2] += 1
    elif answer == "fizz buzz":
        count[3] += 1
    elif answer == "error":
        count[4] += 1
    else:
        count[0] += 1

print("""
Number: {0}\n\
Fizz: {1}\n\
Buzz: {2}\n\
Fizz Buzz: {3}\n\
Error: {4}\n
""".format(count[0],count[1],count[2],count[3],count[4])
      )





