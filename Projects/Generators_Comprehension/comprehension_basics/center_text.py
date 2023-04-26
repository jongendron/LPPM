def center_text(*args):
    # text = ""
    # for arg in args:
    #     text += str(arg) + "-"  # added to end of string, not just items in list
    ## text = '-'.join(args)
    ## text = "-".join(str(arg) for arg in args)  # this is generator expression, not list comprehension
    text = "-".join([str(arg) for arg in args])  # this is list comprehension
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


if __name__ == "__main__":
    center_text("spam and eggs")
    center_text("spam, spam, and eggs")
    center_text(12)
    center_text("spam, spam, spam, and spam")
    center_text("first", "second", 3, 4, "spam")