# These classes are circular and have
# garbage data. Python can handle this to an extent.

class Song:
    """Class to represent a song
    
    Attributes:
    \ttitle (str): The title of the song.
    \tartist (Artist): An artist object representing the song's creator.
    \tduration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """ Class to represent an ASlbum, using it's track list. 
    
    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist will default to an artist with the
            name "Various Artists"
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Usec to add a nw song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self. tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list
        
        Args:
            song (Song): A song to add.
            position (Optional [int]): If specified, the song will be added to that position
                in the track list - inserting it between otehr songs if necessary.
                Otherwise, the song will be added to teh end of the list.
                if position is None
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song) # insert to certain list position


class Artist:
    """Basic class to store artist details.
    
    Attributes:
        name (str): The name of the artist.
        albums (List[Album]): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums.
    Methods:
        add_album: Use to add a new album to the artist's albums list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list
        
        Args:
            album (album): album object to add to the list.
                If the album is already present, it will not be added again
                (although this is yet to be implemented).
        """
        self.albums.append(album)


def find_object(field, object_list):
    """Check `object_list` to see if object with a `name` attribute equal to `field` exists, return it if so.
    `Conflict occures if list contains multiple objects with same name attribute.`"""
    for item in object_list:
        if item.name == field:
            return item
    return None # if nothing found
    # could alternatively use a dictionary for hashing (more efficient)

def load_data(File: str="albums.txt"):
    """Simple program to load Arist/album data from text file.
    """
    new_artist = None
    new_album = None
    artist_list = []

    with open(File, "r") as albums:
        for line in albums:
            # data rows contain (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            #pline = ", ".join([artist_field, album_field, str(year_field), song_field]).rstrip(", ")
            #print(pline)

            if new_artist is None:
                new_artist = Artist(artist_field) # initialize
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # retrieve the artist object if there is one
                # otherwise, create a new artist object and add to artist list.
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                #new_album = None #TODO: Causes new album to be added every time artist changes
                
            if new_album is None: #TODO: If all songs of album are not sequental, two instances of same Album are created and store different tracks (redundant)
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist.
                # Retrieve album object if there is one.
                # otherwise create a new ablumn object and store it in the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)    
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list


def create_checkfile(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}" \
                          .format(new_artist, new_album, new_song),
                            file=checkfile)


if __name__ == '__main__':
    
    #load_data()
    artists = load_data("albums3.txt")
    print("There are {} artists".format(len(artists)))
    
    # Write a new file with artist list to cross-validate against original
    create_checkfile(artists)

