import sqlite3
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter


conn = sqlite3.connect("music.db") # database connection

# When using multiple list boxs and <<ListboxSelect>> as a bound widget
# you must use exportselection=False
# Reference: https://stackoverflow.com/questions/60336671/tkinter-binding-listboxselect-to-function-with-multiple-listboxes-in-frame

# Scrollbox class
class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, **kwargs) # us __init__ from tkinter.Listbox
        
        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview) # command=artistList.yview method scrolls vertically (same for .xview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs) # Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set # tells artistList to call artistScroll.set method whenever anything happens (clicking arrows for example)

def get_albums(event): # bound function call is passed event
    lb = event.widget # retrieve reference to widget that triggers the effect
    print("lb: ", lb, "") # print label box
    index = lb.curselection()[0] # listbox has curselection() that returns tuple of all selected items in the list [0] only lets first value being selected
    # retrieve artist name from listbox curselection
    artist_name = lb.get(index), # The trailing ',' makes the results into a tuple (<value>, ) also works, this is 
    # so it can be input directly into the SQL query substitution

    # get the artist ID from the database row
    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone() # retrieve artist ID by querying name -> returns tuple
    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
        alist.append(row[0])
    albumLV.set(tuple(alist))
    songLV.set(("Choose an album",))


def get_songs(event):
    lb = event.widget
    print("lb: ", lb) # print label box
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get the artist ID from database row
    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
    alist = []
    for row in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
        alist.append(row[0])
    
    songLV.set(tuple(alist))



mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry('1024x768') # pixels

# Configure mainWindow columns
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1) # spacer column on right

# Configure mainWindow rows
mainWindow.rowconfigure(0, weight=1) # title
mainWindow.rowconfigure(1, weight=5) # listbox
mainWindow.rowconfigure(2, weight=5) # listbox
mainWindow.rowconfigure(3, weight=1) # spacer

# labels
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# Artists Listbox
#artistList = tkinter.Listbox(mainWindow)
#artistList = Scrollbox(mainWindow, background='white')
artistList = Scrollbox(mainWindow, background='white', exportselection=False)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
artistList.config(border=2, relief='sunken')

# artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview) # command=artistList.yview method scrolls vertically (same for .xview)
# artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
# artistList['yscrollcommand'] = artistScroll.set # tells artistList to call artistScroll.set method whenever anything happens (clicking arrows for example)

# Populate artist Listbox with data from database
for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    artistList.insert(tkinter.END, artist[0]) # pull artist from tuple

# We want virtual event, <<ListboxSelect>> to find method to it
artistList.bind('<<ListboxSelect>>', get_albums)  # when item is selected from artistList -> use .getalbums() method

# Albums Variable and Listbox
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",)) # to keep all words of string on same line use a tuple
#albumList = tkinter.Listbox(mainWindow, listvariable=albumLV) # link albumList Listbox to albumLV Variable
#albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList = Scrollbox(mainWindow, listvariable=albumLV, exportselection=False)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
albumList.config(border=2, relief='sunken')

albumList.bind('<<ListboxSelect>>', get_songs) # find function to action

# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview) # command=albumList.yview method scrolls vertically (same for .xview)
# albumScroll.grid(row=1, column=1, sticky='nse')
# albumList['yscrollcommand'] = albumScroll.set # tells albumList to call albumScroll.set method whenever anything happens (clicking arrows for example)

# Songs Variable and Listbox
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose a song",))
#songList = tkinter.Listbox(mainWindow, listvariable=songLV) # link songList Listbox to albumLV Variable
#songList = Scrollbox(mainWindow, listvariable=songLV)
songList = Scrollbox(mainWindow, listvariable=songLV, exportselection=False)
songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
songList.config(border=2, relief='sunken')

# Main Loop
testlist = range(0,100)
albumLV.set(tuple(testlist)) # variable and listbox are synced/bound so if variable changes listbox updates (also works when GUI is running)
mainWindow.mainloop()
print("closing database connection")
conn.close()

