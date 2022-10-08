available_exits = ["north", "south", "east", "west"]

chosen_exit = ""    # initialize
while chosen_exit.casefold() not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":    # auto change string case for comparison
        print("Game over")
        break
else:   # If loop doesn't break (when it terminates)
    print("Aren't you glad you got out of there?")