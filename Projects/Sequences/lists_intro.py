computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

print()
print(computer_parts[2]) # prints second item in list

print(computer_parts[0:3]) # slicing produces a subset list
print(computer_parts[-1])  # print last item in list

# lists are mutable and can be changed
# whereas strings are immutable and cannot be changed
