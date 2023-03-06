try:
    import tkinter as tk
except ImportError: # python 2
    import Tkinter as tk

import math

# def parabola(x):
#     y = x * x/100
#     return y


def parabola(page, size):
    # for x in range(-size, size):
    #     y = x*x/size
    #     plot(page, x, y)
    for x in range(size):
        y = x*x/size
        plot(page, x, y)
        plot(page, -x, y)

# TODO: Modify circle function to allow color of circle to be specified
# TODO: and defaults to red color if none is given

def circle(page, radius, g, h, color='red'):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(page):
    page.update() # update the widget / window to show changes
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='grey')
    page.create_line(0, y_origin, 0, -y_origin, fill='grey')
    print('\n', locals())

def plot(page, x, y):
    page.create_line(x,-y, x + 1, -y + 1, fill='orange')


# Test
win = tk.Tk()
win.title('Parabola')
win.geometry("640x480")

# can't draw point, but can do lines of length 1 on canvas
canvas = tk.Canvas(win, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas) # add cartesian axes

# canvas2 = tk.Canvas(win, width=320, height=480, background='blue')
# canvas2.grid(row=0, column=1)
# draw_axes(canvas2)

# print('\n', repr(canvas), '|', repr(canvas2), '\n')

# for x in range(-100, 100):
#     y = parabola(x)
#     plot(canvas, x, -y) # canvas has y-origin starting at top of canvas

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 30, 0, 0, 'blue')
circle(canvas, 10, 30, 30)
circle(canvas, 30, 30, -30, 'purple')

win.mainloop()