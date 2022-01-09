#!/usr/bin/env python3

from tkinter import *
from tkinter import colorchooser 
from gattlib import DiscoveryService, GATTRequester as gr
from random import randint

DEVICE_ID = "21:03:44:00:02:60"
WRITE_HANDLE = 0x0009
READ_HANDLE = 0x000c

scan = DiscoveryService()
devs = scan.discover(2)

if DEVICE_ID not in devs:
    quit()

req = gr(DEVICE_ID)

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
    delay = delay_text.get('1.0', 'end-1c')
    try :
        delay = int(delay)
    except ValueError:
        delay = 4

    mode = light_mode_text.get('1.0', 'end-1c')
    try :
        mode = int(mode)
    except ValueError:
        mode = 1

    if mode > 20 or mode < 1:
        mode = 1

    mode += 36

    req.write_by_handle(WRITE_HANDLE, color_cycle_bytes(mode, delay))  


def lucky():
    if (randint(0, 1)):
        req.write_by_handle(WRITE_HANDLE, color_cycle_bytes(randint(37, 56), randint(0, 50))  
    else:
        req.write_by_handle(WRITE_HANDLE, rgb_to_bytes(randint(0, 255), randint(0, 255), randint(0, 255)))

root = Tk()
col_button = Button(root, text="Select colour", command=custom_rgb)
cycle_button = Button(root, text="Cycle colours", command=colour_cycle)
l = Label(text = "Delay (/200ms)")
delay_text = Text(root, height=1, width=15)
l2 = Label(text = "Light Mode (1 - 20)")
light_mode_text= Text(root, height=1, width=15)
lucky_button = Button(root, text="I'm feeling lucky", command=lucky)

col_button.pack()
l.pack()
delay_text.pack()
l2.pack()
light_mode_text.pack()
cycle_button.pack()
lucky_button.pack()

root.geometry("350x200")
root.mainloop()
