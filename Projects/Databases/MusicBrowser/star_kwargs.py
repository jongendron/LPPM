# def print_backwards(*args, file=None): # uses a predefined kwarg (with default)
#     """Reverses all words and order of words"""
#     for word in args[::-1]:
#         print(word[::-1], end=' ', file=file)

# with open("backwards.txt", 'w') as backwards:    
    #print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards)

# What if our function is based on another function that is capable of taking multiple different arguements
# Also, what if that function changes to a later version that has more arguements? How would we account for this?
# **** kwargs **** is the answer! **kwargs unpacks a dictionary rather than a tuple of values.
# Note: when unpacking a dict with "**" function you can pass it to a function (ex Function1(**<dict>)) to use each key-value pair as a kwarg!
# -> but the keyword arguements provided mut be useful to the function, therefore print(**<dict>) will produce nothing unless <dict> contains keys that are meaninful

#def print_backwards(*args, end=' ', **kwargs): # Option1: end= will no longer be part of kwargs dict if end is specificied explicitly
def print_backwards(*args, **kwargs): # uses a predefined kwarg (with default)
    """Reverses all words and order of words"""
    # TODO: Challenge - What happens if calling code specifies a kwarg that the function is already using? (Solve this)
    # -> it will through a TypeError: got multiple values for keyword arguement 'end'
    # -> for example, we need to suppress EOL character arguement for example
    #print(kwargs)
    
    # Option2: remove what you want directlt from kwargs
    #kwargs.pop('end', None) # replace end and return None (if key doesn't exist still returns None)

    # Option3: Specify default keys and remove keys from dictionary logical test
    print_kwargs = {'end': ' '}
    for key, value in kwargs.items():
        #print("*" * 60)
        #print(r"{}: {}".format(key, value))
        
        # Option3a: logical testing
        if key not in print_kwargs: # ceed input kwarg to values coded into the function for print()
            print_kwargs[key] = value
            #print("Added '{}: '{}' to print_kwargs.".format(key, value))

        # Option3b: try block and exceptions
        # try:
        #     print_kwargs[key]
        # except KeyError:
        #     print("Kwarg was not in defined dict. Adding to dict.")
        #     print_kwargs[key] = value
        # else:
        #     print("Kwarg already existed in dict.")


    for word in args[::-1]:
        #print(word[::-1], end=' ', **kwargs) # recall **<dict> unpacks the dictionary
        print(word[::-1], **print_kwargs)

# with open("backwards.txt", 'w') as backwards:    
#     print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", file=backwards, sep='\n', end='\n')

#print("Hello", "planet", "earth", "take", "me", "to", "your", "leader", sep='|', end='\n')
#print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", sep='|', end='\n')

def print_backwards2(*args, **kwargs):
    end_character = kwargs.pop('end', '\n') # return '\n' if no value found
    sep_character = kwargs.pop('sep', ' ') # return ' ' if no value found
    #for word in args[::-1]:
    for word in args[:0:-1]: # stops before 0
        print(word[::-1], end=sep_character, **kwargs)
    #print(end=end_character) # which means we don't need this line
    print(args[0][::-1], end=end_character, **kwargs) # print firt word separately

    # TODO: Could also loop through words and join them to single list or tuple and use only 1 print

print("Hello", "planet", "earth", "take", "me", "to", "your", "leader", sep='\n**\n', end='\n')
print_backwards2("Hello", "planet", "earth", "take", "me", "to", "your", "leader", sep='\n**\n', end='\n')

# TODO: Could also subclass of print?

# TODO: Using list comprehension

def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs) # using list comprehension 

print("*" * 60)
backwards_print("Hello", "planet", "earth", "take", "me", "to", "your", "leader", sep='\n**\n', end='\n')


