# -------------------------------------------
# Potential issues when using any() and all()
# -------------------------------------------
# entries = [1, 2, 3, 4, 5]

entries = []

if entries:
    print("all: {}".format(all(entries)))  # True:
else:
    print("all: False")
print("any: {}".format(any(entries)))  # True: any item has a True value

# result = entries and all(entries) # incorrect
result = bool(entries) and all(entries) # correct
print(result)