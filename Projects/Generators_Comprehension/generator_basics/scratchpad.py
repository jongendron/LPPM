# efficient way to swap 2 values
a = 2
b = 3

print(f"a is {a}, b is {b}")

# right hand side is evaluate first
a, b = b, a  # swaps values w/o temporary variable

print(f"a is {a}, b is {b}")