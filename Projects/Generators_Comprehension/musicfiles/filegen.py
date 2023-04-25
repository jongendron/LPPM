# ----------------------------------------------------------------------
# experimenting with the os.walk() generator to parse files on hard disc
# ----------------------------------------------------------------------
import os

root = "./musicfiles/music"

# os.walk() recursivly visits every directory from root, and returns a tuple
for path, directories, files in os.walk(root, topdown=True):
    if files:        
        print("*" * 40)
        print(path)  # generator position path
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split(' - ')  # [:-5] -> remove extension (.emp3)
            print(song_details)
        input()
    # print(directories)  # directories in the path
    # print(files)  # files in the path
    # input()
    # for f in files:
    #     print(f"\t{f}")