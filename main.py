#!/usr/bin/env python3

from tkinter import *
from tkinter import colorchooser 
from gattlib import DiscoveryService, GATTRequester as gr

DEVICE_ID = "21:03:44:00:02:60"
WRITE_HANDLE = 0x0009
READ_HANDLE = 0x000c

"""
scan = DiscoveryService()
devs = scan.discover(2)

if DEVICE_ID not in devs:
    quit()

req = gr(DEVICE_ID)
"""

def rgb_to_bytes(r, g, b):
    return bytes(bytearray([0x56, int(hex(r), 16), int(hex(g), 16), int(hex(b), 16), 0x00, 0xf0, 0xaa]))

# light mode range (25 - 38); 01 speed is 200ms hence 05 is 1 second
# default color_cycle_bytes(25, 5)
def color_cycle_bytes(light_mode, delay):
    return bytes(bytearray([0xbb, int(hex(light_mode), 16), int(hex(delay), 16), 0x44]))

def custom_rgb():
    col = colorchooser.askcolor(title="Select colour")
    if None in col:
        return

    r = int(col[0][0])
    g = int(col[0][1])
    b = int(col[0][2])
    req.write_by_handle(WRITE_HANDLE, rgb_to_bytes(r, g, b))

def colour_cycle():
    req.write_by_handle(WRITE_HANDLE, color_cycle_bytes(25, 5))  

root = Tk()
col_button = Button(root, text="Select colour", command=custom_rgb)
cycle_button = Button(root, text="Cycle colours", command=colour_cycle)
col_button.pack()
cycle_button.pack()
root.geometry("350x200")
root.mainloop()
