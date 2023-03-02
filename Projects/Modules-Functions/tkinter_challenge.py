# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter
import os

#TODO: Do you have to set the weight of rows and columns in the mainWindow as well as in Framewindows?
#TODO: try not creating a frame and just using cells and columns

# Create simple blank window
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("640x480+8+200") # widnows size and position
mainWindow['padx'] = 24 # padding of all rows/cols
mainWindow['pady'] = 24

# Configure rows and columns as grid
row_num = 6
col_num = 4
row_wts = (1,1,1,1,1,1)
col_wts = (1,1,1,1)

# Can't figure out the damn weight for all the buttons because they are too small

#lv1 = range(0, row_num)
#lv2 = range(0, col_num)
#print(len(lv1) == len(row_wts) and len(lv2) == len(col_wts))

#configure each row with row_wts
for row in range(0,row_num):
    mainWindow.rowconfigure(row, weight=row_wts[row])

#configure each col with row_wts
for col in range(0, col_num):
    mainWindow.columnconfigure(col, weight=col_wts[col])

# Input/Output Bar
IO_entry = tkinter.Entry(mainWindow)
IO_entry.grid(row=0, column=0, columnspan=4, sticky='nsew', pady=(12,12))
IO_entry.config(relief='sunken')

# Create frame for buttons
#Button_frame = tkinter.Frame(mainWindow)
#Button_frame.grid(row=1, column=0, rowspan=5, columnspan=4, sticky='nsew')

# Create Buttons
#'Labels' : ['name', 'row', 'col', 'rspan', 'colspan', 'sticky'],
button_dict = {
    'b_C' : ['C', 1, 0, 1, 1,'nsew'],
    'b_CE' : ['CE', 1, 1, 1, 1,'nsew'],
    'b_7' : ['7', 2, 0, 1, 1,'nsew'],
    'b_8' : ['8', 2, 1, 1, 1,'nsew'],
    'b_9' : ['9', 2, 2, 1, 1,'nsew'],
    'b_pl' : ['+', 2, 3, 1, 1,'nsew'],
    'b_4' : ['4', 3, 0, 1, 1,'nsew'],
    'b_5' : ['5', 3, 1, 1, 1,'nsew'],
    'b_6' : ['6', 3, 2, 1, 1,'nsew'],
    'b_mn' : ['-', 3, 3, 1, 1,'nsew'],
    'b_1' : ['1', 4, 0, 1, 1,'nsew'],
    'b_2' : ['2', 4, 1, 1, 1,'nsew'],
    'b_3' : ['3', 4, 2, 1, 1,'nsew'],
    'b_st' : ['*', 4, 3, 1, 1,'nsew'],
    'b_0' : ['0', 5, 0, 1, 1,'nsew'],
    'b_eq' : ['=', 5, 1, 1, 2,'nsew'],
    'b_bs' : ['/', 5, 3, 1, 1,'nsew']
}

# Create bottons
for key in button_dict:
    bdata = button_dict[key]
    #tkinter.Radiobutton(Button_frame, text=bdata[1], value=bdata[0], variable=rbValue
    #                    ).grid(row=bdata[2], column=bdata[3], rowspan=bdata[4], columnspan=bdata[5])
    tkinter.Button(mainWindow, text=bdata[0]
                   ).grid(row=bdata[1], column=bdata[2], rowspan=bdata[3], columnspan=bdata[4], sticky=bdata[5])

mainWindow.mainloop()

