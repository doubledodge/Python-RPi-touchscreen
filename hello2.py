"""
Forget all the nice Object Oreintd Programming for now 
and just throw a few lables and control buttons on to a
tkinter screen to test out the cheap QUIMAT touch screen
with the I2C 32 GPIO priopedia interace also plugged in
"""
import tkinter as tk     
from tkinter import ttk
# access the i2c 32xGPIO interface
import smbus
bus = smbus.SMBus(0) # 0 for the original RPi, 1 for the newer version
# using the I2C 32 GPIO priopedia interace set all of J23 to outputs
bus.write_byte_data(0x20,0x00,0x00)
# now set up the touch screen control buttons for the first output on J23
win = tk.Tk()            
win.title("RPi GUI")  
# Add a helpful Label
ttk.Label(win, text="Test GPIO interface").grid(column=0, row=0)
# A dirty bodge to put a bit of space into the window
ttk.Label(win, text="").grid(column=0, row=1)
ttk.Label(win, text="").grid(column=0, row=3)
ttk.Label(win, text="").grid(column=0, row=5)

# Modified Button Click Functions
def clickOn():
    bus.write_byte_data(0x20,0x12,0x01)
def clickOff():
    bus.write_byte_data(0x20,0x12,0x00)

# Adding a Button
action1 = ttk.Button(win, text="Click on", command=clickOn)
# Position Button in second row,  column 2 (zero-based)
action1.grid(column=0, row=2)
# Adding a Button
action2 = ttk.Button(win, text="Click off", command=clickOff)
# Position Button 
action2.grid(column=0, row=4)
# Adding a Button
action3 = ttk.Button(win, text="QUIT", command=quit)
# Position Button 
action3.grid(column=0, row=6)
# Start the touch screen interface
win.mainloop()
