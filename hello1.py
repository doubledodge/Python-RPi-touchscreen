#! /usr/bin/python  
# -*- coding: utf-8 -*-
""" 
This is a simple Hello World example from the 
Tkinter module in section 24.1.2.2 of the  Python documentation
This example also has a neat window exit button
The Tkinter module (“Tk interface”) is the standard Python 
interface to the Tk GUI toolkit 
"""
# from Tkinter import * provided in the example but the following is better
from Tkinter import Button, Tk, Frame
class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
# this has a nice window close button
