try:
    import tkinter
except ImportError: # python 2
    import Tkinter as Tkinter

# Check Versions
print()
print(tkinter.TkVersion)
print(tkinter.TclVersion)
print()

# Test it works (test 1)
#tkinter._test()

# Create simple blank window (test 2)
mainWindow = tkinter.Tk()
mainWindow.title("Main Window")
mainWindow.geometry("640x480+164+400") # string not ints
mainWindow.mainloop()

# Geometry managers