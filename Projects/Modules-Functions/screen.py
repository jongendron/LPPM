import tkinter
import os

# Create simple blank window (test 2)
mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480+8+200") # string not ints
mainWindow['padx'] = 8

label = tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=100)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1000)
mainWindow.columnconfigure(3, weight=600)
mainWindow.columnconfigure(4, weight=1000)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2) # spans 2 rows completely
fileList.config(border=2, relief='sunken')

#mainWindow.mainloop()

# Populate filelist
#for zone in os.listdir('/usr/bin'):
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone) # tkinter.END inserts entries at end of list

# Create vertical scroll bar
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview) # command=fileList.yview -> vertical scroll
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)

# Link vertical scroll bar to file list
fileList['yscrollcommand'] = listScroll.set

# frame for the radio buttons (options for display)
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details') # nice for adding radio buttons
optionFrame.grid(row=1, column=2, sticky='ne')

#mainWindow.mainloop()

rbValue = tkinter.IntVar() # three radio buttons that share same variable -> only 1 selection allowed
rbValue.set(3) # default option

radio1 = tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)

radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

mainWindow.mainloop()

# Entry widget to show result of radio button's effect on files in filelist
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, stick='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=3, column=0, sticky='new')

# time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59) # alternative method
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59) # must use 'from_' not 'from'

hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
secondSpinner.grid(row=0, column=4)

timeFrame['padx'] = 36 # centers/pads contents of this widget on x-axis

# Frame for date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Date labels
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')

dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May',\
                                                        'Jun', 'Jul', 'Aug', 'Sep',\
                                                             'Oct', 'Nov', 'Dec'))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)

daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

dateFrame['padx'] = 36

# Buttons
okButton = tkinter.Button(mainWindow, text='OK')
#cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit) # closes gui down (don't call .quit(), just us .quit)
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.destroy) # do not run function to run before .Button is called (.destroy() is wrong)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

print(rbValue.get())