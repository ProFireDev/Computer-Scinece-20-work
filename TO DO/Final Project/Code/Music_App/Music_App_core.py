#importing all of the basic things we will need
from tkinter import *
import tkinter as tk
import pygame, threading
import audio_metadata, time
from mutagen.mp3 import MP3
import os
#defult dimentions of the application window
height = 695
width = 1092

#setting up the main window

windows = tk.Tk()
windows.title("CS 20 Final project - Music Player")

screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()

#centering stuff, woo!

x = int((screen_width/2) - (width/2))
y = int((screen_height/2) - (height/2))

windows.geometry("{}x{}+{}+{}".format(width, height, x, y))
windows.config(bg='#222222') #setting up the defult window background for dark theme

background = Label(windows, borderwidth=0)
background.place(x=0,y=0)

root=Frame(windows, height=height, width=width)
root.pack()
def window():   
    wintype = windows.state()
    if wintype == 'zoomed':
        temp = screen_height // 100
        temp = temp * 100
        var = temp - 620
        padding = var // 2
        root.pack(pady=padding)
        
    elif wintype == 'normal':
        root.config(highlightthickness=0)
        root.pack(pady=0)
    root.after(100, window)


##############################################################################################
#                              APPLICATION LAYOUT:









#starts the actual code
windows.mainloop()