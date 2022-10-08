# Backwards slicing
# start value must be greater than stop value
# does not include end target
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]    # z -> b by -1 index slice
print(backwards)
backwards = letters[25:-1:-1]    # negative stop values start backwards from end up sequence
print(backwards)
backwards = letters[::-1]    # reversing idiom
print(backwards)

# Challenges
print()
print(letters[16:13:-1])        # qpo
print(letters[4::-1])           # edcba
print(letters[25:(25-8):-1])    # last 8 in reverse
print(letters[:-9:-1])          # same

# Common idioms
print()
print(letters[::-1])    # reverse
print(letters[-4:])     # (end - n) to end (n = 4 in this case)
print(letters[:1])      # 0 to n (n = 1 here)
print(letters[0])       # first element

# if letters were empty [:1] does not crash with index error
letters2 = ""
print(letters2[:1])
print(letters2[0])


