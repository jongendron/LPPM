activity = input("What would you like to do today? ")

# .casefold() will covert the sequence to all lowercase characters
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
