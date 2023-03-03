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

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5) # essential to make sure buttons fillup the screen
mainWindow.columnconfigure(0, weight=1)

mwPadx = 10
mwPady = 10
mainWindow['padx'] = mwPadx
mainWindow['pady'] = mwPady

# Create output layer
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='news', pady=10)

# Create Frame for buttons
keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='news')
keyPad.columnconfigure(tuple(range(4)), weight=1)
keyPad.rowconfigure(tuple(range(5)), weight=1)

# Create keypad button dictionary
#'Labels' : ['name', 'row', 'col', 'rspan', 'colspan', 'sticky'],
sticky_set = 'news'
buttons = {
    'b_C' : ['C', 0, 0, 1, 1,sticky_set],
    'b_CE' : ['CE', 0, 1, 1, 1,sticky_set],
    'b_7' : ['7', 1, 0, 1, 1,sticky_set],
    'b_8' : ['8', 1, 1, 1, 1,sticky_set],
    'b_9' : ['9', 1, 2, 1, 1,sticky_set],
    'b_pl' : ['+', 1, 3, 1, 1,sticky_set],
    'b_4' : ['4', 2, 0, 1, 1,sticky_set],
    'b_5' : ['5', 2, 1, 1, 1,sticky_set],
    'b_6' : ['6', 2, 2, 1, 1,sticky_set],
    'b_mn' : ['-', 2, 3, 1, 1,sticky_set],
    'b_1' : ['1', 3, 0, 1, 1,sticky_set],
    'b_2' : ['2', 3, 1, 1, 1,sticky_set],
    'b_3' : ['3', 3, 2, 1, 1,sticky_set],
    'b_st' : ['*', 3, 3, 1, 1,sticky_set],
    'b_0' : ['0', 4, 0, 1, 1,sticky_set],
    'b_eq' : ['=', 4, 1, 1, 2,sticky_set],
    'b_bs' : ['/', 4, 3, 1, 1,sticky_set]
}

# Insert buttons to keyPad (Frame)
button_list = []
for key in buttons:
    button = buttons[key]
    button_obj = tkinter.Button(keyPad, text=button[0])
    button_obj.grid(row=button[1], column=button[2],\
            rowspan=button[3], columnspan=button[4],\
            sticky=button[5])
    button_obj.configure(relief='raised')
    button_list.append(button_obj)

mainWindow.update()

mainWindow.minsize(keyPad.winfo_width() + mwPadx,\
    result.winfo_height() + keyPad.winfo_height() + mwPady)

mainWindow.maxsize(keyPad.winfo_width() + mwPadx + 50,\
    result.winfo_height() + keyPad.winfo_height() + mwPady + 50)

mainWindow.mainloop()
