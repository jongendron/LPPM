# --------------------------------------------------------------------------
# takes iteratable and returns True or False based on values of the iterable
# 'True' values are equal to 1, 'False' values are equal to 0
# -> This is based on boolean tests/expressions.
# --------------------------------------------------------------------------

entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))  # True: all items have True values
print("any: {}".format(any(entries)))  # True: any item has a True value
print()

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))  # False: 0 is not a 'True' value
print("any: {}".format(any(entries_with_zero)))  # True: at least one 'True' value
print()

print("=" * 80)

# Bool() confirms how Python interprets an object
print("Values interpreted as False in Python")
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({}))
)

print("=" * 80)

name = ""
if name:
    print("Hello {}.".format(name))
else:
    print("Welcome, person with no name.")
