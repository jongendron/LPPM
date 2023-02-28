import tkinter

# Create simple blank window (test 2)
mainWindow = tkinter.Tk()
mainWindow.title("Main Window")
mainWindow.geometry("640x480+164+200") # string not ints

label = tkinter.Label(mainWindow, text="Hello World")
#label.pack(side='top')
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
#leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
#canvas.pack(side='left', fill=tkinter.Y) # positon canvas to left but fill X-axis doesn't work
#canvas.pack(side='left', fill=tkinter.Y) # positon canvas to left and fill Y-axis
#canvas.pack(side='left', fill=tkinter.X, expand=True) # expand is required to fill X-axis
#canvas.pack(side='top', fill=tkinter.X) # not required on top or bottom though
#canvas.pack(side='top', fill=tkinter.Y, expand=True) # expand is required to fill X-axis if side is top/bottom
#canvas.pack(side='top')
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
#rightFrame.pack(side='right', anchor='n', expand=True)
rightFrame.grid(row=1, column=2, sticky='n') # sticky ~ anchor

button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')

#button1.pack(side='top')
button1.grid(row=0, column=0)
#button2.pack(side='left')
button2.grid(row=1, column=0)
#button3.pack(side='right')
button3.grid(row=2, column=0)

# confiure the column
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1) # col 0 is entire space
button2.grid(sticky='ew')

mainWindow.mainloop()