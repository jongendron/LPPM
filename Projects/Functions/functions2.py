# Function Definitions

# Multiply Function
def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.
    Although this function is intended to multiply two numbers, you can also use it to multiply a sequence.
    If you pass a string, for example, as the first argument, the function outputs the string repeated 'y' times.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result # if not specified the function returns 'None'


# Removes white space, punctuation, periods, and commas from string
def extract_char(string):
    rvm_list = [" ","\t","\n",".",",","!",":",";","?"]
    l0 = []
    for char in string:
        if char not in rvm_list:
            l0.append(char)
    return "".join(l0)


# Checks if a word is a palindrone
def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards and backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1] # reverse string (last element to first by -1 (read right to left)
    # return backwards == string # check if reverse string is same as original (True or False)
    # return string[::-1] == string
    return string[::-1].casefold() == string.casefold() # convert to lower case to remove case sensitivity


# Method 1: Use lookup list
# def is_palindrome_sentence(string):
#     # print(extract_char(string)[::-1].casefold(),extract_char(string).casefold(),sep="\n")
#     return extract_char(string)[::-1].casefold() == extract_char(string).casefold()


# Method 2: Use .isalnum() method of a string to return only alphabetical or numerical values (alpha-numeric)
def is_palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.
    The function ignores whitespace, capitalisation, and punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string) # check 1
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string) # can call user defined functions within


# Uses function annotation and docstring annotation
def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n` ."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1): # -1 because we are setting the first iteration value
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result

# Main Code

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
#
# print()

# sentence0 = input("Please enter a sentence to check: ")
# if is_palindrome_sentence(sentence0):
#     print("'{}' is a palindrome".format(sentence0))
# else:
#     print("'{}' is not a palindrome".format(sentence0))

# answer = multiply(18,3)
# print(answer)

for i in range(-1):
    print(i,fibonacci(i))

# p = is_palindrome() # now arguemnet class shows up when calling function
p = is_palindrome_sentence(242)
p = fibonacci()





