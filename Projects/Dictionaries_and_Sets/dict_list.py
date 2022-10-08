available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive"
}

computer_parts = []
current_choice = None
chosen_part = None
while current_choice != "0":
    if current_choice in available_parts: # only checks the keys of dict, not values
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}") # fstring: object goes in {}
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}") # fstring: object goes in {}
            computer_parts.append(chosen_part)
        print("Your list now contains: {}"
              .format(computer_parts))
    else:
        print("Please Select a key from the following dictionary of parts:")
        print("%-3s %-10s" % ("key", "part"))
        for key, part in available_parts.items():
            print("%-3s %-10s" % (key, part))
        print("%-3s %-10s" % ("0", "To finish"))

    current_choice = input("> ")

print("Your parts list: {}".format(", ".join(computer_parts)))
