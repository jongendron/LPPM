import sqlite3
try:
    import tkinter
except ImportError: # python 2
    import Tkinter as tkinter

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


class DataListBox(Scrollbox):
    
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scollbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.linked_box = None  # linked child widget
        self.link_field = None  # field linked with parent widget
        self.link_value = None # id for link_field of parent widget's current selection

        self.cursor = connection.cursor() # work with cursors rather than connection directly
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)  # bind <<ListboxSelect>> event to self.on_select method

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order) # separated sort fields by comma
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self): # clear data out of list box
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):  # links target listbox to this master listbox
        self.linked_box = widget  # reference to target listbox
        widget.link_field = link_field  # field to link widgets together by

    def requery(self, link_value=None):
        self.link_value = link_value  # store the id, so we know the "master" record we're poulated from        
        if link_value and self.link_field:  # ensures there is infact a linked field between two listboxes
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            # print(sql)  # TODO: delte this line
            self.cursor.execute(sql, (link_value,))
        else:
            # print(self.sql_select + self.sql_sort)  # TODO: delete this line after testing
            self.cursor.execute(self.sql_select + self.sql_sort)

        # Clear listbox contents -> then repopulate
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0]) # first item in tuple should be target value

        if self.linked_box: # deletes contents of linked listbox # Note the linked listbox must have clear method!
            self.linked_box.clear()
            self.linked_box.insert(tkinter.END, "Select an Album")

    def on_select(self, event):
        """method to select item from gui, then use its value to requery the linked database."""
        
        if self.linked_box:
            # print(self is event.widget)  # TODO: self should be the same as event.widget (event.widget points to it).
            if self.curselection(): # test that curselection() isn't empty
                index = self.curselection()[0] # listbox has curselection() that returns tuple of all selected items in the list [0] only lets first value being selected    
                value = self.get(index), # retrieve artist name from listbox curselection (',' makes it tuple)                

                # get the ID from the database row
                # make sure we are getting the correct one, by including link_value if appropriate
                sql_on_select = self.sql_select + " WHERE " + self.field + "=?"               
                if self.link_value:
                    value = value[0], self.link_value
                    sql_on_select = sql_on_select + " AND " + self.link_field + "=?"                  
                
                # print(sql_on_select)  # TODO: delete this line
                print(value)  # TODO: delete this line
                link_id = self.cursor.execute(sql_on_select, value).fetchone()[1]  # _id should be second column of tuple | this grabs first row                    
                # print(f"link_id: {link_id}")  # TODO: delete this line
                self.linked_box.requery(link_id)
                # self.linked_box.link_value = link_id  # if you want to store the link_value after on_select (jon version)
 
    
if __name__ == "__main__":
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

    # Labels
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ===== Artists Listbox =====
    artistList = DataListBox(mainWindow, connection=conn, table="artists", field="name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
    artistList.config(border=2, relief='sunken')
    artistList.requery()

    # ===== Albums Listbox & Variable =====
    # albumLV = tkinter.Variable(mainWindow)
    # albumLV.set(("Choose an artist",)) # to keep all words of string on same line use a tuple

    albumList = DataListBox(mainWindow, connection=conn, table="albums", field="name", sort_order=("name",))
    #albumList = DataListBox(mainWindow, connection=conn, table="albums", field="name", sort_order=("name",), listvariable=albumLV)
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
    albumList.config(border=2, relief='sunken')
    # albumList.requery(12)

    artistList.link(albumList, "artist")

    # ===== Songs Variable and Listbox =====
    # songLV = tkinter.Variable(mainWindow)
    # songLV.set(("Choose a song",))

    songList = DataListBox(mainWindow, connection=conn, table="songs", field="title", sort_order=("track", "title"))
    # songList = DataListBox(mainWindow, connection=conn, table="songs", field="title", sort_order=("track", "title"), listvariable=songLV)
    songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
    songList.config(border=2, relief='sunken')
    # songList.requery()

    albumList.link(songList, "album")

    # ===== Main Loop =====
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()

