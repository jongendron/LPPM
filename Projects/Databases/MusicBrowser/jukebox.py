import sqlite3
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter


conn = sqlite3.connect("music.db") # database connection

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
artistList = tkinter.Listbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
artistList.config(border=2, relief='sunken')

artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview) # command=artistList.yview method scrolls vertically (same for .xview)
artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
artistList['yscrollcommand'] = artistScroll.set # tells artistList to call artistScroll.set method whenever anything happens (clicking arrows for example)

# Albums Variable and Listbox
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",)) # to keep all words of string on same line use a tuple
albumList = tkinter.Listbox(mainWindow, listvariable=albumLV) # link albumList Listbox to albumLV Variable
albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
albumList.config(border=2, relief='sunken')

albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview) # command=albumList.yview method scrolls vertically (same for .xview)
albumScroll.grid(row=1, column=1, sticky='nse')
albumList['yscrollcommand'] = albumScroll.set # tells albumList to call albumScroll.set method whenever anything happens (clicking arrows for example)

# Songs Variable and Listbox
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = tkinter.Listbox(mainWindow, listvariable=songLV) # link songList Listbox to albumLV Variable
songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
songList.config(border=2, relief='sunken')

# Main Loop
testlist = range(0,100)
albumLV.set(tuple(testlist)) # variable and listbox are synced/bound so if variable changes listbox updates (also works when GUI is running)
mainWindow.mainloop()
print("closing database connection")
conn.close()

