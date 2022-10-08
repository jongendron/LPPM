albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Compay", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984)
          ]
print(len(albums))

# for album in albums:
#     print("Album: {}, Artist: {}, Year {}" # fill {} in order
#            .format(albums[0], albums[1], albums[2])
#           )
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

# Can could alternative unpack a nested lists as well
