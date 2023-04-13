# Write a program that recieves a number from user input and converts it to an integer
import sys, atexit # triggers exit code at exit of program

exit_code = 0

def exit_handler():
    print(f"\nProgram exited with code {exit_code}")


def getint(prompt: str) -> int:
    """Receives standard input from user and conerts to integer. Handles invalid input by raising an excepion and looping through until valid input is provided."""
    while True:
        try:
            #number = int(input("Please enter a number: "))
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again.")
        except EOFError:
            exit_code = 1
            sys.exit(exit_code) # terminates program


atexit.register(exit_handler)

# First determine potential exceptions/errors
# Option 1, do testing!
# Option 2, read documentation: https://docs.python.org/3/library/exceptions.html
# x = int(input("Enter a number: ")) # ValueError is potential exception

# main 
if __name__ == "__main__":
    #print(getint())
    
    while True:
        print("*" * 60)
        num1 = getint("Please enter dividend: ")
        num2 = getint("Please enter divisor: ")

        try:
            print(f"{num1} divided by {num2} is {num1/num2}")
        except ZeroDivisionError:
            print("You can't divide by zero")
            exit_code = 2
            sys.exit(exit_code)





