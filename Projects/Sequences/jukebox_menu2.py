# Challenge:
# Reprint the album list and or song list if invalid option is chosen
from nested_data import albums

# Constants
SONGS_LIST_INDEX = 3 # Constant: this constant is used to index 4th item of list
SONG_TITLE_INDEX = 1 # index of song titles

# while True:
#     print("Please choose your album (invalid choice exits):")
#
#     # Print only album index and name
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index + 1, title))
#
#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         songs_list = albums[choice - 1][SONGS_LIST_INDEX] # use the index constant
#     else:
#         break
#
#     print("Please choose your song:")
#     for index, (track_number, song) in enumerate(songs_list):
#         print("{}: {}".format(index + 1, song)) # plus one to range 1:#songs
#
#     song_choice = int(input())
#     if 1 <= song_choice <= len(songs_list):
#         title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
#         print("Playing {}".format(title))
#
#     print("=" * 40) # divider for clearer output

stop_prog = False
while not stop_prog:
    valid_album = False
    while not valid_album:
        print("Please choose your album (invalid choice exits):")
        # Print only album index and name
        for index, (title, artist, year, songs) in enumerate(albums):
            print("{}: {}".format(index + 1, title))
        print("0: Exit Program")
        choice = int(input())
        if choice == 0:
            break
        elif 1 <= choice <= len(albums):
            songs_list = albums[choice - 1][SONGS_LIST_INDEX] # use the index constant
            # song_choice = int(input())
            valid_song = False
            while not valid_song:
                print("Please choose your song:")
                for index, (track_number, song) in enumerate(songs_list):
                    print("{}: {}".format(index + 1, song))
                print("0: Back to Albums")
                song_choice = int(input())
                if song_choice == 0:
                    break
                elif 1 <= song_choice <= len(songs_list):
                    title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
                    print("Playing {}".format(title))
                    valid_song = True
                else:
                    print("Invalid Choice ->")
        else:
            print("Invalid Choice ->")


    print("=" * 40)



