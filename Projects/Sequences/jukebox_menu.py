# First import album list from previous Python file
# but remember that Python executes all code from imported file by default
from nested_data import albums

# Constants
SONGS_LIST_INDEX = 3 # Constant: this constant is used to index 4th item of list
SONG_TITLE_INDEX = 1 # index of song titles

while True:
    print("Please choose your album (invalid choice exits):")

    # This throws an error because enumerate returns 2 element tuple not 5 elements
    # for index, title, artist, year, songs in enumerate(albums):
    #     print("{}: {}, {}, {}, {}"
    #           .format(index + 1, title, artist, year, songs))

    # # enumerate() returns a tuple of (index, value) -> this unpacks it
    # for index, value in enumerate(albums):
    #     # print(index, value) # This prints an int and tuple
    #     # value is also a tuple that we can unpack
    #     title, artist, year, songs = value
    #     print(index, title, artist, year,songs)

    # # We can also unpack enumerate and value directly using ()'s
    # for index, (title, artist, year, songs) in enumerate(albums):
    #     print("{}: {}, {}, {}, {}"
    #         .format(index + 1, title, artist, year, songs))

    # Print only album index and name
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX] # use the index constant
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song)) # plus one to range 1:#songs

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    else:
        break

    print("Playing {}".format(title))
    print("=" * 40) # divider for clearer output



