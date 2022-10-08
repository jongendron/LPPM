available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive"
}

current_choice = None
chosen_part = None
computer_parts = {}     # creates empty dict

while current_choice != "0":
    if current_choice in available_parts: # only checks the keys of dict, not values
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in there, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part # current_choice is 1:6
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please Select a key from the following dictionary of parts:")
        print("%-3s %-10s" % ("key", "part"))
        for key, part in available_parts.items():
            print("%-3s %-10s" % (key, part))
        print("%-3s %-10s" % ("0", "To finish"))

    current_choice = input("> ")
