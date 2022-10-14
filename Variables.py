# Imports Tkinter, a built-in Python GUI Library
from tkinter import *
# Imports the 'messagebox' sub-module from Tkinter so that messages can be displayed
from tkinter import messagebox
# Imports the italic sub-module from 'tkinter.font' so that italic fonts can be displayed 
from tkinter.font import BOLD, ITALIC

import ctypes, os, sys
from os.path import exists

# Colours
white = "#ffffff"
lgrey = "#f0f0f0"
grey = "#333639"
black = "#000000"

red = "#db6050"
green = "#67e6bb"
blue = "#3d8fcc"

# Font(s)
font = "Trebuchet MS"

# Declaring and Configuring the Window
win = Tk()

win.attributes("-fullscreen", True)
win.configure(bg = "white")

# UI Icons
logoutIcon = PhotoImage(file = "Icons/Logout.png")
loginIcon = PhotoImage(file = "Icons/Login.png")
regIcon = PhotoImage(file = "Icons/Register.png")
exitIcon = PhotoImage(file = "Icons/Cross.png")
homeIcon = PhotoImage(file = "Icons/Home.png")
enterIcon = PhotoImage(file = "Icons/Enter.png")
welcomeIcon = PhotoImage(file = "Icons/Menu.png")

# Quiz Icons
compSciIcon = PhotoImage(file = "Icons/CPU.png")
mathsIcon = PhotoImage(file = "Icons/Maths.png")
flagsIcon = PhotoImage(file = "Icons/Flag.png")

# Flags Images
easyQ3Img = PhotoImage(file = "Questions and Answers/Flags/Easy/q3.png")
easyQ3 = easyQ3Img.subsample(10, 10)

easyQ5Img = PhotoImage(file = "Questions and Answers/Flags/Easy/q5.png")
easyQ5 = easyQ5Img.subsample(10, 10)

medQ1Img = PhotoImage(file = "Questions and Answers/Flags/Medium/q1.png")
medQ1 = medQ1Img.subsample(10, 10)

medQ4Img = PhotoImage(file = "Questions and Answers/Flags/Medium/q4.png")
medQ4 = medQ4Img.subsample(10, 10)

hardQ2Img = PhotoImage(file = "Questions and Answers/Flags/Hard/q2.png")
hardQ2 = hardQ2Img.subsample(10, 10)

hardQ3Img = PhotoImage(file = "Questions and Answers/Flags/Hard/q3.png")
hardQ3 = hardQ3Img.subsample(10, 10)

hardQ5Img = PhotoImage(file = "Questions and Answers/Flags/Hard/q5.png")
hardQ5 = hardQ5Img.subsample(10, 10)