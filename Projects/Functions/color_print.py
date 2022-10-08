import colorama # Allows ANSI escape sequences on windows

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# print(RED, "this will be in red...")
# print("\tand so is this")


def color_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change color, etc.
    :param text: The text to print.
    :param effects: The effects we want. One or more of the constants defined
        at the start of this module.
    """
    effect_string = "".join(effects) # effects goes from tupple -> string to be used as 1 arg in next line
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


colorama.init()  # activate colorama (ANSI for windows)
color_print("Hello, Red", RED)
color_print("Hello, Red in bold", RED, BOLD)
# test that the colour was reset
print("This should be in the default terminal colour")
color_print("Hello, Blue", BLUE)
color_print("Hello, Blue reversed", BLUE, REVERSE)
color_print("Hello, Blue reversed and underlined", BLUE, REVERSE, UNDERLINE)
color_print("Hello, Yellow", YELLOW)
color_print("Hello, Yellow bold", YELLOW, BOLD)
color_print("Hello, Bold", BOLD)
color_print("Hello, Underline", UNDERLINE)
color_print("Hello, Reverse", REVERSE)
color_print("Hello, Black", BLACK)
colorama.deinit() # deactivate colorama (ANSI for windows)

