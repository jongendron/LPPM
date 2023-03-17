# These classes are circular and have
# garbage data. Python can handle this to an extent.

#TODO: Modify the program so that the class structure matches the simplified diagram:
# Artist objects can hold references to Album objects, and Album objects can hold references
# to Song objects.

class Song:
    """Class to represent a song
    
    Attributes:
    \ttitle (str): The title of the song.
    \tartist (str): The name of the song's creater.
    \tduration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        #self.name = title
        self.artist = artist        
        self.duration = duration

    def get_title(self):
        return self.title
        
    name = property(get_title) # `getter` for title (Song.name is now same as Song.title)


class Album:
    """ Class to represent an Album, using it's track list. 
    
    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (str): The name of the artist responsible for the album. If not specified,
            the artist will default to the name "Various Artists".
        tracks (List[Song]): A list of the songs on the album.

    Methods:
        addSong: Usec to add a nw song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            #self.artist = Artist("Various Artists") # circular reference
            self.artist = "Various Artists" # non circular reference
        else:
            self.artist = artist
            #self.artist = artist.name

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list
        
        Args:
            song (Song): The title of the song to add.
            position (Optional [int]): If specified, the song will be added to that position
                in the track list - inserting it between otehr songs if necessary.
                Otherwise, the song will be added to teh end of the list.
                if position is None
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)

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

    def add_song(self, name, year, title):
        """Add new song to the collection of albums
        
        This method will add the song to an album in the collection.
        A new album will be created in teh collection if it doesn't exist.

        Args:
            name (str): The name of the album
            year (int): The year the album was produced
            title (str): The title of the song
        """
        album_found = find_object(name, self.albums) # finds address of object to edit
        if album_found is None:
            #print(name + " not found")
            #album_found = Album(name, year, self) # causes circular reference to artist class
            album_found = Album(name, year, self.name) # removes circular reference of artist class
            self.add_album(album_found)
        else:
            #print("Found album " + name)
            pass

        album_found.add_song(title) # TODO: Does this point to the album with the artist object
        # could/should I alternatively call on self?
        # self.album[?] instead of album_found? or just use the pointer?
        # I think because this pointer is temporily created within the
        # -> .add_song() method, and because we don't loop through
        # -> different data inputs within the method, then
        # -> it is a valid pointer!


def find_object(field, object_list):
    """Check `object_list` to see if object with a `name` attribute equal to `field` exists, return it if so.
    `Conflict occures if list contains multiple objects with same name attribute`.
    If the output is saved to an object, it will have same address at location found
    from this query."""
    for item in object_list:
        if item.name == field:
            return item
    return None # if nothing found
    # could alternatively use a dictionary for hashing (more efficient)

def load_data(File: str="albums.txt"):
    """Simple program to load Arist/album data from text file.
    """

    artist_list = []

    with open(File, "r") as albums:
        for line in albums:
            # data rows contain (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            #pline = ", ".join([artist_field, album_field, str(year_field), song_field]).rstrip(", ")
            #print(pline)

            new_artist = find_object(artist_field, artist_list) # essentially a pointer
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            # Focus on artists (.add_song() doesn't exist yet)
            new_artist.add_song(album_field, year_field, song_field)

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

