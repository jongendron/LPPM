def banner_text(text: str = " ", screen_width: int = 80) -> None: # screen width has default
    """
    Print a string centered, with ** on either side.

    :param text: string of text to use as banner.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at the
        left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    # screen_width = width # 80 is default
    if len(text) > screen_width - 4:
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text,screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


width = 100
banner_text("*",screen_width=width)
banner_text("Always look on the bright side of life",screen_width=width)
banner_text("If life seems jolly rotten,",screen_width=width)
banner_text("There's something you've forgotten!",screen_width=width)
banner_text("And that's to laugh and smile and dance and sing,",screen_width=width)
# banner_text(" ",screen_width=width)
banner_text(screen_width=width) # default value of text is " " (space)
# keyword arguement screen_width must be used above or else text is blank
banner_text("When you're feeling in the dumps,",screen_width=width)
banner_text("Don't be silly chumps,",screen_width=width)
banner_text("Just purse your lips and whistle - that's the thing!",screen_width=width)
banner_text("And... always look on the bright side of life...",screen_width=width)
banner_text("*",screen_width=width)

# # When a function does have a defined return, it will return none
# print()
# numbers = [5,3,1,2]
# print(numbers)
# print(numbers.sort()) # will return none because of function
# print(numbers) # will print the sorted number list