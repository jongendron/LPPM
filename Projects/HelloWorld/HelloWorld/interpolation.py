# interpolation strings
age = 26
print("My age is %d years" % age)
print()

# replacement is left to right with no repeats
# % in the string specifies the replacement location(s)
# %() after string specifies the replacements
# %s = string; %d = digit (int); %f = float %x (hecidecimal)
# %-f will do left align
# %f will do right align by default
major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximately %-f" % (22 / 7))
print("PI is approximately %-60.50f" % (22 / 7))