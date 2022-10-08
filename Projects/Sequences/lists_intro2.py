computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

# Replace single element (item) of mutable sequence with another using slice
#computer_parts[3] = "trackball"
#print(computer_parts)

# Replace slice with an interable (object that can be looped over)
print(computer_parts[3:]) # print mouse and mouse mat
#computer_parts[3:] = "trackball"
#print(computer_parts) # replaced by contents of iterable
computer_parts[3:] = ["trackball"] # turn "trackball" string into single item list
print(computer_parts) # replaces all remaining items in list with single item list