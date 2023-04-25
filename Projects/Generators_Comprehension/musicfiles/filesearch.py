# --------------------------------------
# 2023-04-24
# relies on file and directory structure
# --------------------------------------

import os
import fnmatch  # matches files/directories who's names follow a pattern

def find_albums(root, artist_name):
    """Generator that parses hard disc for files pertaining to `artist_name`. Requires hierarchial file system structure.
    Hierarchy: <root>/<artist>/<album>/<song>
    """
    for path, directories, files in os.walk(root):        
        caps_name = artist_name.upper()
        # for artist in directories:
        # for artist in fnmatch.filter(directories, artist_name):  # filters directories list so it matches artist_name
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):  # comprehension generator
            subdir = os.path.join(path, artist)  # joins one path with another subpath
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album  # returns path to album's songs and album name


def find_songs(albums):  # albums is a generator of albums -> produces tuple(<album_path>, <album_name>)
    """Generator that parses the output from the generator find_albums"""
    for album in albums:  # requestes <album_path>, <album_name> on demand (never all in memory!)
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song  # prevents need to save working master list


if __name__ == "__main__":
    album_list = find_albums("musicfiles/music", "black*")  # using Regex expression (case sensitive on linux)
    song_list = find_songs(album_list)
    
    # for a in album_list:
        # print(a)

    # Chaining generators together by passing 1 generator as argument to next
    for s in song_list:
        print(s)
