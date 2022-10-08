import random   # imports random module

highest = 10
answer = random.randint(1, highest)  # dot notation: module.function
print(answer)   # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0               # initialized
guesses = 0             # starts with 1 guess

while guess != answer:
    guess = int(input())    # no prompt
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
