# ------------------------------
# Challenge: Create a generator that will return
#   The complete filename of all <extension> files.
#   It should start at a specified directory (start)
#   The filenames should include the full path from
#   the specified start directory -> returns relative
#   path. Make it generic so you can provide any ext.
# id3reader library: https://nedbatchelder.com/code/modules/id3rader.html
# -> helps you read id3 format binary for tags 
# ------------------------------

import os
import fnmatch
import id3reader_p3 as id3reader

# My solution
# def file_search(root: str, ext: str):
#     """Generator to find files with specified extension `ext`."""
#     for path, _, files in os.walk(root):
#         if files:
#             for file in files:
#                 # if file[-len(ext):] is ext:  # use == not is
#                 if file[-len(ext):] == ext:
#                     yield os.path.join(path, file), file
#                     abs_path = os.path.abspath(path)
#                     yield os.path.join(abs_path, file), file


# Tim's solution
def file_search(root, ext):
    for path, dirs, files in os.walk(root):
        for file in fnmatch.filter(files, f'*.{ext}'):  # filter to only include files with extension
            # yield os.path.join(path, file), file
            abs_path = os.path.abspath(path)
            yield os.path.join(abs_path, file), file  # absolute path


if __name__ == "__main__":
    root = "musicfiles/music"
    ext = "emp3"
    

    # Creating a generator first
    # songs = file_search(root, ext)
    # for song in songs:
    #     print(song)

    # Creating a temporary generator
    error_files = []
    for song in file_search(root, ext):
        # print(song)
        try:
            id3r = id3reader.Reader(song[0])
        # except OSError:
        except:  # In this case, any error is acceptable (contrary to convention)
            error_files.append(song[0])
        else:
            print("Artist: {}, Album {}:, Track: {}, Song: {}".format(
                id3r.get_value('performer'),
                id3r.get_value('album'),
                id3r.get_value('track'),
                id3r.get_value('title')
            ))

    print('*' * 60)
    print("Files with incorrect format:")
    for efile in error_files:
        print(f'\t{efile}')
                