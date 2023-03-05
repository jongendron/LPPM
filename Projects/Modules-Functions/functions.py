def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


#def center_text(*args, width=80, sep=' ', end='\n', file=None, flush=False): # *args denotes variable number inputs
def center_text(*args, width=80, sep=' '):
    #text = str(text) # convert to string to get character length
    text = ""
    for arg in args:
        text += str(arg) + sep # concat all args into single string sep by space

    text = text.rstrip(sep)
    left_margin = (width - len(text)) // 2
    #print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text

# call the function
# with open("centered", mode='w') as centered_file:
#     #print(python_food()) # result of function is printed and is actually 'None'
#     center_text("spam and eggs", file=centered_file)
#     center_text("spam, spam, and eggs", file=centered_file)
#     center_text("spam, spam, spam, and spam", file=centered_file)
#     center_text(1, "hello", "this is my text", sep=":", file=centered_file)

with open('menu.txt', 'w') as menu:
    s1 = center_text("spam and eggs")
    #s2 = center_text("spam, spam, and eggs")
    s3 = center_text("spam, spam, spam, and spam")
    s4 = center_text(1, "hello", "this is my text", sep=":")
    print(s1, file=menu)
    #print(s2)
    print(center_text("spam, spam, and eggs"), file=menu)
    print(s3, file=menu)
    print(s4, file=menu)

# print("=" + str(12 * 3))
# print(sorted(["b", "d", "c", "a"]))