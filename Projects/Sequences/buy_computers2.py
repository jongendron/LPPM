# initialize variables
available_parts = [
    "computer",
    "monitor",
    "keyboard",
    #"mouse",
    "mouse mat",
    "hdmi cable",
    "dvd drive"
]

#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)

current_choice = "-"    # initialize a string with "-" and link to object
computer_parts = []     # initialize an list (creates empty list)

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below to your list:")
        # Method 1: Use a for loop and use .index method to test if each item in list equals the target (inefficient)
        #for part in available_parts:
            # .format(available_parts).index(part) finds index position of part in available_parts
            # print("{0}: {1}".format(available_parts.index(part) + 1, part))

        # Method 2: Loop over list using two variables v1 = index position of item, v2 = item
        # enumerate returns the index position and item
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)