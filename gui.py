#!/usr/bin/env python3

# Python program to create color chooser dialog box

# importing tkinter module
from tkinter import *

# importing the choosecolor package
from tkinter import colorchooser

WRITE_HANDLE = 0x0009

def rgb_to_bytes(r, g, b):
    return bytes(bytearray([0x56, int(hex(r), 16), int(hex(g), 16), int(hex(b), 16), 0x00, 0xf0, 0xaa]))


# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
# variable to store hexadecimal code of color
    col = colorchooser.askcolor(title ="Choose color")
    if None in col:
        print("r is none")
        return
    else: 
        print(col)

    r = int(col[0][0])
    g = int(col[0][1])
    b = int(col[0][2])
    # req.write_by_handle(WRITE_HANDLE, rgb_to_bytes(r, g, b))
    print(WRITE_HANDLE, rgb_to_bytes(r, g, b))


root = Tk()
button = Button(root, text = "Select color",
            command = choose_color)
button.pack()
root.geometry("300x100")
root.mainloop()


