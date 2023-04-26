text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]  # capitalize all characters
print(capitals)
# print("".join(capitals))

words = [word.upper() for word in text.split(' ')]  # split by space and capitalize
print(words)

# lc_words = [word for word in text.split(' ')]  # no need for comprehension if you don't need to process each iteration
lc_words = text.split(' ')
print(lc_words)