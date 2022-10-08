welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
bad = "Bad Compay", "Bad Company", 1974
budgie = ("Nightflight", "Budgie", 1981)
imelda = "More Mayhem", "Emilda May", 2011
metallica = ("Ride the Lightning", "Metallica", 1984)

print(metallica)
print(metallica[0]) # indexing still uses []'s
print(metallica[1])
print(metallica[2])

# Ways Tuples can be useful:
# Tuples use less memory than lists
# Tuples protect the integrity of your data
# because code will crash when you try to change it\

# metallica[0] = "Master of Puppets" # can't assign value inplace
metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)