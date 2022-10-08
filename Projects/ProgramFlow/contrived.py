#numbers = [1, 45, 31, 16, 60]
numbers = [1,45,7,2,5]
# else is associated with for loop not if statement
for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")

# This will cause the condition on line 3 to be false, and the loop will terminate. When a loop terminates normally, the else block is executed.