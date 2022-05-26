# Imports Tkinter, a built-in Python GUI Library
from tkinter import *
# Imports the 'messagebox' sub-module from Tkinter so that messages can be displayed
from tkinter import messagebox
# Imports the italic sub-module from 'tkinter.font' so that italic fonts can be displayed 
from tkinter.font import BOLD, ITALIC

import ctypes, os, sys
from os.path import exists


# Adjusts the DPI of the Window so text does not appear pixelated
ctypes.windll.shcore.SetProcessDpiAwareness(1)

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


# --- MISC. FUNCTIONS ---
def exit():
    win.destroy()
    sys.exit()

def delete():
    askDelete = messagebox.askyesno("Delete account!", "Are you sure you want to delete your account?")

    if askDelete == YES:
        os.remove(f"Accounts/{usernameIn}.txt")
        os.remove(f"Highscores/{usernameIn}.txt")

        main()

    else:
        pass

# --- FLAGS FUNCTIONS ---
def flagsEasy():
    # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
    for widget in win.winfo_children():
        widget.destroy()

    score = 0

    # -- QUESTION 1 FUNCTIONS --
    def q1opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore + 1

        q2()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q1opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect Answer!", "There are actually 50 stars on the flag of the USA.")

    def q1():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Easy/Question 1/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Easy/Question 1/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Easy/Question 1/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 1: Flags (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {score}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q1opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q1opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 2 FUNCTIONS --
    def q2opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore + 1

        q3()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q2opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "Both Switzerland and The Vatican City (actually a country) have a square-shaped flag.")

    def q2():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Easy/Question 2/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Easy/Question 2/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Easy/Question 2/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 2: Flags (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {oneScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q2opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optTwo, borderwidth = 0, command = q2opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 3 FUNCTIONS
    def q3opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Incorrect answer!", "That is the flag of Nepal.")

    def q3opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore + 1

        q4()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q3():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Easy/Question 3/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Easy/Question 3/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Easy/Question 3/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 3: Flags (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {twoScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = easyQ3, bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q3opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optTwo, borderwidth = 0, command = q3opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 4 FUNCTIONS --
    def q4opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "Purple is the least used colour in national flags.")

    def q4opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore + 1

        q5()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q4():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Easy/Question 4/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Easy/Question 4/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Easy/Question 4/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 4: Flags (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {threeScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q4opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optTwo, borderwidth = 0, command = q4opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 5 FUNCTIONS --
    def q5opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore + 1

        int(fiveScore)

        end()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q5opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        int(fiveScore)

        end()
        messagebox.showerror("Incorrect answer!", "That is the national flag of Sweden.")

    def q5():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Easy/Question 5/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Easy/Question 5/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Easy/Question 5/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 5: Flags (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {fourScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = easyQ5, bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q5opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optTwo, borderwidth = 0, command = q5opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- END SCREEN FUNCTION --
    def end():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()


        # Updates highscore if necessary
        f = open(f"Highscores/{usernameIn}.txt", "r")
        line = f.readlines()
        prevHighscore = line[1]

        if int(fiveScore) >= int(prevHighscore):
            f = open(f"Highscores/{usernameIn}.txt", "w")

            f.write("Flags (Easy)\n")
            f.write(str(fiveScore))
            
        else:
            pass


        # Title
        Label(win, image = flagsIcon, text = " Flags (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        str(fiveScore)

        # Overall score label
        Label(win, text = f"Well done! You scored {fiveScore} / 5.", bg = white, fg = grey, font = (font, 18)).pack()

        # Calculate percentage earned
        int(fiveScore)
        percentage = (fiveScore / 5) * 100

        # Percentage label
        Label(win, text = f"(That's {percentage}%)", bg = white, fg = grey, font = (font, 10, ITALIC)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Back 2 home label
        Label(win, text = f"Click the button below to go back home", bg = white, fg = grey, font = (font, 12)).pack()

        # Another home button
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    q1()

def flagsMedium():

    score = 0

    # -- QUESTION 1 FUNCTIONS --
    def q1opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect Answer!", "That is the flag of Switzerland!.")

    def q1opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect Answer!", "That is the flag of Switzerland!.")

    def q1opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore + 1

        q2()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q1():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Medium/Question 1/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Medium/Question 1/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Medium/Question 1/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Medium/Question 1/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 1: Flags (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {score}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = medQ1, bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q1opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q1opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q1opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 2 FUNCTIONS --
    def q2opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect Answer!", "New Zealand's flag has 4 stars.")

    def q2opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect Answer!", "New Zealand's flag has 4 stars.")

    def q2opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore + 1

        q3()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q2():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Medium/Question 2/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Medium/Question 2/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Medium/Question 2/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Medium/Question 2/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 2: Flags (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {oneScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q2opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q2opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q2opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 3 FUNCTIONS --
    def q3opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore + 1

        q4()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q3opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Incorrect Answer!", "Red is, by far, the most common colour on national flags.")

    def q3opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Incorrect Answer!", "Red is, by far, the most common colour on national flags.")

    def q3():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Medium/Question 3/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Medium/Question 3/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Medium/Question 3/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Medium/Question 3/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 3: Flags (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {twoScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q3opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q3opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q3opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 5 FUNCTIONS --
    def q4opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect Answer!", "That is the flag of Syria.")

    def q4opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore + 1

        q5()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q4opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect Answer!", "That is the flag of Syria.")

    def q4():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Medium/Question 4/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Medium/Question 4/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Medium/Question 4/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Medium/Question 4/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 4: Flags (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {threeScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = medQ4, bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q4opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q4opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q4opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # -- QUESTION 5 FUNCTIONS --
    def q5opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Inorrect answer!", "The Greek flag consists of only blue and white.")

    def q5opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Inorrect answer!", "The Greek flag consists of only blue and white.")

    def q5opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore + 1

        end()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q5():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Medium/Question 5/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Medium/Question 5/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Medium/Question 5/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Medium/Question 5/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 5: Flags (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {fourScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q5opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q5opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q5opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


# -- END SCREEN FUNCTION --
    def end():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()


        # Updates highscore if necessary
        f = open(f"Highscores/{usernameIn}.txt", "r")
        line = f.readlines()
        prevHighscore = line[1]

        if int(fiveScore) >= int(prevHighscore):
            f = open(f"Highscores/{usernameIn}.txt", "w")

            f.write("Flags (Medium)\n")
            f.write(str(fiveScore))
            
        else:
            pass


        # Title
        Label(win, image = flagsIcon, text = " Flags (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        str(fiveScore)

        # Overall score label
        Label(win, text = f"Well done! You scored {fiveScore} / 5.", bg = white, fg = grey, font = (font, 18)).pack()

        # Calculate percentage earned
        int(fiveScore)
        percentage = (fiveScore / 5) * 100

        # Percentage label
        Label(win, text = f"(That's {percentage}%)", bg = white, fg = grey, font = (font, 10, ITALIC)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Back 2 home label
        Label(win, text = f"Click the button below to go back home", bg = white, fg = grey, font = (font, 12)).pack()

        # Another home button
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    q1()

def flagsHard():
    
    score = 0

    def q1opt4():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect answer!", "A vexillologist is a person who studies flags.")

    def q1opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore + 1

        q2()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q1opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect answer!", "A vexillologist is a person who studies flags.")

    def q1opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect answer!", "A vexillologist is a person who studies flags.")

    def q1():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Hard/Question 1/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Hard/Question 1/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Hard/Question 1/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Hard/Question 1/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Flags/Hard/Question 1/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]


        # Title
        Label(win, image = flagsIcon, text = " Question 1: Flags (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {score}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q1opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q1opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q1opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = q1opt4, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def q2opt4():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "That is the national flag of Liechtenstein.")

    def q2opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "That is the national flag of Liechtenstein.")

    def q2opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore + 1

        q3()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q2opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "That is the national flag of Liechtenstein.")

    def q2():
         # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Hard/Question 2/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Hard/Question 2/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Hard/Question 2/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Hard/Question 2/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Flags/Hard/Question 2/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]


         # Title
        Label(win, image = flagsIcon, text = " Question 2: Flags (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {oneScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = hardQ2, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q2opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q2opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q2opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = q2opt4, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def q3opt4():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore + 1

        q4()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q3opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Inorrect answer!", "That is Andorra's national flag.")

    def q3opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Inorrect answer!", "That is Andorra's national flag.")

    def q3opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Inorrect answer!", "That is Andorra's national flag.")

    def q3():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Hard/Question 3/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Hard/Question 3/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Hard/Question 3/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Hard/Question 3/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Flags/Hard/Question 3/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]


         # Title
        Label(win, image = flagsIcon, text = " Question 3: Flags (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {twoScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = hardQ3, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q3opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q3opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q3opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = q3opt4, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def q4opt4():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "Denmark's national flag is the oldest flag in the world.")

    def q4opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "Denmark's national flag is the oldest flag in the world.")

    def q4opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "Denmark's national flag is the oldest flag in the world.")

    def q4opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore + 1

        q5()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q4():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Hard/Question 4/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Hard/Question 4/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Hard/Question 4/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Hard/Question 4/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Flags/Hard/Question 4/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]


         # Title
        Label(win, image = flagsIcon, text = " Question 4: Flags (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {threeScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q4opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q4opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q4opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = q4opt4, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def q5opt4():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore + 1

        end()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def q5opt3():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Incorrect answer!", "That is the flag of the Marshall Islands.")

    def q5opt2():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Incorrect answer!", "That is the flag of the Marshall Islands.")

    def q5opt1():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Incorrect answer!", "That is the flag of the Marshall Islands.")

    def q5():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Flags/Hard/Question 5/Question.txt", "r")
        o1 = open(f"Questions and Answers/Flags/Hard/Question 5/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Flags/Hard/Question 5/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Flags/Hard/Question 5/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Flags/Hard/Question 5/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]


         # Title
        Label(win, image = flagsIcon, text = " Question 5: Flags (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {fourScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Flag picture
        Label(win, image = hardQ5, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = q5opt1, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = q5opt2, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = q5opt3, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = q5opt4, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def end():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()


        # Updates highscore if necessary
        f = open(f"Highscores/{usernameIn}.txt", "r")
        line = f.readlines()
        prevHighscore = line[1]

        if int(fiveScore) >= int(prevHighscore):
            f = open(f"Highscores/{usernameIn}.txt", "w")

            f.write("Flags (Hard)\n")
            f.write(str(fiveScore))
            
        else:
            pass


        # Title
        Label(win, image = flagsIcon, text = " Flags (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        str(fiveScore)

        # Overall score label
        Label(win, text = f"Well done! You scored {fiveScore} / 5.", bg = white, fg = grey, font = (font, 18)).pack()

        # Calculate percentage earned
        int(fiveScore)
        percentage = (fiveScore / 5) * 100

        # Percentage label
        Label(win, text = f"(That's {percentage}%)", bg = white, fg = grey, font = (font, 10, ITALIC)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Back 2 home label
        Label(win, text = f"Click the button below to go back home", bg = white, fg = grey, font = (font, 12)).pack()

        # Another home button
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    q1()

def flagsModeSelection():
   # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
    for widget in win.winfo_children():
        widget.destroy()

    # Title
    Label(win, image = flagsIcon, text = " Flags", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Easy button
    Button(win, text = "Easy", borderwidth = 0, command = flagsEasy, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Medium button
    Button(win, text = "Medium", borderwidth = 0, command = flagsMedium, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Hard button
    Button(win, text = "Hard", borderwidth = 0, command = flagsHard, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
    # Logout button
    Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # To Dashboard Icon
    Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


# --- COMPUTER SCIENCE FUNCTIONS ---
def compSciEasy():

    score = 0

    def oneCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore + 1

        q2()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def oneWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Inorrect answer!", "The clock speed is measured in Hertz (Hz).")

    def q1():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Easy/Question 1/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Easy/Question 1/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Easy/Question 1/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 1: Computer Science (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {score}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = oneCorrect, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = oneWrong, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def twoCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore + 1

        q3()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def twoWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "The two types of memory are ROM and RAM.")

    def q2():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Easy/Question 2/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Easy/Question 2/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Easy/Question 2/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 2: Computer Science (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {oneScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = twoCorrect, bg = grey, fg = white, width = 20, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = twoWrong, bg = grey, fg = white, width = 20, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def threeCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore + 1

        q4()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def threeWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Inorrect answer!", "A LAN is a Local Area Network.")

    def q3():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Easy/Question 3/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Easy/Question 3/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Easy/Question 3/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 3: Computer Science (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {twoScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = threeWrong, bg = grey, fg = white, width = 20, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = threeCorrect, bg = grey, fg = white, width = 20, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def fourCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore + 1

        q5()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def fourWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "Malware is malicious software designed to harm a computer.")

    def q4():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Easy/Question 4/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Easy/Question 4/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Easy/Question 4/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 4: Computer Science (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {threeScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = fourWrong, bg = grey, fg = white, width = 45, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = fourCorrect, bg = grey, fg = white, width = 45, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def fiveCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore + 1

        end()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def fiveWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Incorrect answer!", "A backup is a spare copy of data in case the data is lost.")

    def q5():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Easy/Question 5/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Easy/Question 5/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Easy/Question 5/Option 2.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 5: Computer Science (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {fourScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = fiveWrong, bg = grey, fg = white, width = 22, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = fiveCorrect, bg = grey, fg = white, width = 22, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def end():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()


        # Updates highscore if necessary
        f = open(f"Highscores/{usernameIn}.txt", "r")
        line = f.readlines()
        prevHighscore = line[1]

        if int(fiveScore) >= int(prevHighscore):
            f = open(f"Highscores/{usernameIn}.txt", "w")

            f.write("Computer Science (Easy)\n")
            f.write(str(fiveScore))
            
        else:
            pass


        # Title
        Label(win, image = compSciIcon, text = " Computer Science (Easy)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        str(fiveScore)

        # Overall score label
        Label(win, text = f"Well done! You scored {fiveScore} / 5.", bg = white, fg = grey, font = (font, 18)).pack()

        # Calculate percentage earned
        int(fiveScore)
        percentage = (fiveScore / 5) * 100

        # Percentage label
        Label(win, text = f"(That's {percentage}%)", bg = white, fg = grey, font = (font, 10, ITALIC)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Back 2 home label
        Label(win, text = f"Click the button below to go back home", bg = white, fg = grey, font = (font, 12)).pack()

        # Another home button
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    q1()

def compSciMedium():

    score = 0

    def oneCorrect():
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore + 1

        q2()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def oneWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Inorrect answer!", "A core is a processing unit within the CPU.")

    def q1():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Medium/Question 1/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Medium/Question 1/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Medium/Question 1/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Medium/Question 1/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 1: Computer Science (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {score}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = oneWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = oneCorrect, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = oneWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def twoCorrect():
        global twoScore

        int(oneScore)

        twoScore = oneScore + 1

        q3()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def twoWrong():
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "Flash memory is used for secondary storage.")

    def q2():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Medium/Question 2/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Medium/Question 2/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Medium/Question 2/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Medium/Question 2/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 2: Computer Science (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {oneScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = twoWrong, bg = grey, fg = white, width = 28, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = twoWrong, bg = grey, fg = white, width = 28, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = twoCorrect, bg = grey, fg = white, width = 28, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def threeCorrect():
        global threeScore

        int(twoScore)

        threeScore = twoScore + 1

        q4()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def threeWrong():
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Incorrect answer!", "Secondary storage is mainly used to store data long-term.")

    def q3():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Medium/Question 3/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Medium/Question 3/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Medium/Question 3/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Medium/Question 3/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 3: Computer Science (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {twoScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = threeCorrect, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = threeWrong, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = threeWrong, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def fourCorrect():
        global fourScore

        int(threeScore)

        fourScore = threeScore + 1

        q5()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def fourWrong():
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "The two network models are client-server and peer-to-peer.")

    def q4():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Medium/Question 4/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Medium/Question 4/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Medium/Question 4/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Medium/Question 4/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 4: Computer Science (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {threeScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = fourWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = fourWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = fourCorrect, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def fiveCorrect():
        global fiveScore

        int(fourScore)

        fiveScore = fourScore + 1

        end()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def fiveWrong():
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Inorrect answer!", "A protocol is a set of rules that govern how a network communicates.")

    def q5():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Medium/Question 5/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Medium/Question 5/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Medium/Question 5/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Medium/Question 5/Option 3.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 5: Computer Science (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {fourScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = fiveCorrect, bg = grey, fg = white, width = 44, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = fiveWrong, bg = grey, fg = white, width = 44, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = fiveWrong, bg = grey, fg = white, width = 44, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def end():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()


        # Updates highscore if necessary
        f = open(f"Highscores/{usernameIn}.txt", "r")
        line = f.readlines()
        prevHighscore = line[1]

        if int(fiveScore) >= int(prevHighscore):
            f = open(f"Highscores/{usernameIn}.txt", "w")

            f.write("Computer Science (Medium)\n")
            f.write(str(fiveScore))
            
        else:
            pass


        # Title
        Label(win, image = compSciIcon, text = " Computer Science (Medium)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        str(fiveScore)

        # Overall score label
        Label(win, text = f"Well done! You scored {fiveScore} / 5.", bg = white, fg = grey, font = (font, 18)).pack()

        # Calculate percentage earned
        int(fiveScore)
        percentage = (fiveScore / 5) * 100

        # Percentage label
        Label(win, text = f"(That's {percentage}%)", bg = white, fg = grey, font = (font, 10, ITALIC)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Back 2 home label
        Label(win, text = f"Click the button below to go back home", bg = white, fg = grey, font = (font, 12)).pack()

        # Another home button
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    q1()

def compSciHard():

    score = 0

    def oneCorrect():
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore + 1

        q2()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def oneWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global oneScore

        int(score)

        orgScore = score
        oneScore = orgScore

        q2()
        messagebox.showerror("Incorrect answer!", "The three types of buses are the address, control and data buses.")

    def q1():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Hard/Question 1/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Hard/Question 1/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Hard/Question 1/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Hard/Question 1/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Computer Science/Hard/Question 1/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 1: Computer Science (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {score}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = oneWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = oneCorrect, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = oneWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = oneWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def twoCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore + 1

        q3()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def twoWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global twoScore

        int(oneScore)

        twoScore = oneScore

        q3()
        messagebox.showerror("Incorrect answer!", "The program counter holds the address of the next instruction to be fetched.")

    def q2():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Hard/Question 2/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Hard/Question 2/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Hard/Question 2/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Hard/Question 2/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Computer Science/Hard/Question 2/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 2: Computer Science (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {oneScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = twoWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = twoWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = twoWrong, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = twoCorrect, bg = grey, fg = white, width = 32, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def threeCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore + 1

        q4()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def threeWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global threeScore

        int(twoScore)

        threeScore = twoScore

        q4()
        messagebox.showerror("Incorrect answer!", "Virtual memory is secondary storage used as additional RAM.")

    def q3():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Hard/Question 3/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Hard/Question 3/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Hard/Question 3/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Hard/Question 3/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Computer Science/Hard/Question 3/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 3: Computer Science (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {twoScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = threeWrong, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = threeWrong, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = threeCorrect, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = threeWrong, bg = grey, fg = white, width = 36, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def fourCorrect():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore + 1

        q5()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def fourWrong():
        # With the 'global' method, variables declared in the function can be used elsewhere
        global fourScore

        int(threeScore)

        fourScore = threeScore

        q5()
        messagebox.showerror("Incorrect answer!", "Routers send signals across the internet.")

    def q4():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Hard/Question 4/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Hard/Question 4/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Hard/Question 4/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Hard/Question 4/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Computer Science/Hard/Question 4/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 4: Computer Science (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {threeScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = fourWrong, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = fourCorrect, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = fourWrong, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = fourWrong, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def fiveCorrect():
         # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore + 1

        end()
        messagebox.showinfo("Correct answer!", "You have selected the correct answer.")

    def fiveWrong():
         # With the 'global' method, variables declared in the function can be used elsewhere
        global fiveScore

        int(fourScore)

        fiveScore = fourScore

        end()
        messagebox.showerror("Incorrect answer!", "The hexadecimal number system is used to create a MAC Address.")

    def q5():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()

        q = open(f"Questions and Answers/Computer Science/Hard/Question 5/Question.txt", "r")
        o1 = open(f"Questions and Answers/Computer Science/Hard/Question 5/Option 1.txt", "r")
        o2 = open(f"Questions and Answers/Computer Science/Hard/Question 5/Option 2.txt", "r")
        o3 = open(f"Questions and Answers/Computer Science/Hard/Question 5/Option 3.txt", "r")
        o4 = open(f"Questions and Answers/Computer Science/Hard/Question 5/Option 4.txt", "r")
        
        qLine = q.readlines()
        o1Line = o1.readlines()
        o2Line = o2.readlines()
        o3Line = o3.readlines()
        o4Line = o4.readlines()

        question = qLine[0]
        optOne = o1Line[0]
        optTwo = o2Line[0]
        optThree = o3Line[0]
        optFour = o4Line[0]

        # Title
        Label(win, image = compSciIcon, text = " Question 5: Computer Science (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # Score label
        Label(win, text = f"Score: {fourScore}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

        # Question label
        Label(win, text = question, bg = white, fg = grey, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 1 button
        Button(win, text = optOne, borderwidth = 0, command = fiveWrong, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 2 button
        Button(win, text = optTwo, borderwidth = 0, command = fiveWrong, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 3 button
        Button(win, text = optThree, borderwidth = 0, command = fiveWrong, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Option 4 button
        Button(win, text = optFour, borderwidth = 0, command = fiveCorrect, bg = grey, fg = white, width = 40, height = 2, font = (font, 12)).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    def end():
        # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
        for widget in win.winfo_children():
            widget.destroy()


        # Updates highscore if necessary
        f = open(f"Highscores/{usernameIn}.txt", "r")
        line = f.readlines()
        prevHighscore = line[1]

        if int(fiveScore) >= int(prevHighscore):
            f = open(f"Highscores/{usernameIn}.txt", "w")

            f.write("Computer Science (Hard)\n")
            f.write(str(fiveScore))
            
        else:
            pass


        # Title
        Label(win, image = compSciIcon, text = " Computer Science (Hard)", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        str(fiveScore)

        # Overall score label
        Label(win, text = f"Well done! You scored {fiveScore} / 5.", bg = white, fg = grey, font = (font, 18)).pack()

        # Calculate percentage earned
        int(fiveScore)
        percentage = (fiveScore / 5) * 100

        # Percentage label
        Label(win, text = f"(That's {percentage}%)", bg = white, fg = grey, font = (font, 10, ITALIC)).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # A placeholder
        Label(win, text = "", bg = white).pack()

        # Back 2 home label
        Label(win, text = f"Click the button below to go back home", bg = white, fg = grey, font = (font, 12)).pack()

        # Another home button
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


        # Exit button
        Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
        # Logout button
        Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

        # To Dashboard Icon
        Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    q1()

def compSciModeSelection():
    # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
    for widget in win.winfo_children():
        widget.destroy()

    # Title
    Label(win, image = compSciIcon, text = " Computer Science", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Easy button
    Button(win, text = "Easy", borderwidth = 0, command = compSciEasy, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Medium button
    Button(win, text = "Medium", borderwidth = 0, command = compSciMedium, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Hard button
    Button(win, text = "Hard", borderwidth = 0, command = compSciHard, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()


    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
    # Logout button
    Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

    # To Dashboard Icon
    Button(win, image = homeIcon, borderwidth = 0, command = dashboard, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


# --- HOMEPAGE FUNCTION ---

# So I initially called this the 'dashboard' rather than the 'homepage', so this is why the function is still called 'dashboard'
def dashboard():
    # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
    for widget in win.winfo_children():
        widget.destroy()

    # Finds your highscore and in what subject you got that highscore in
    f = open(f"Highscores/{usernameIn}.txt", "r")
    line = f.readlines()
    highSubject = line[0]
    currentHighscore = line[1]


    # Title
    Label(win, image = homeIcon, text = f" Homepage", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = f"Your highscore is {currentHighscore} / 5 in {highSubject}", bg = white, fg = grey, font = (font, 12)).pack(anchor = W)

    # Geography quiz button
    Button(win, text = "Computer Science", borderwidth = 0, command = compSciModeSelection, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Flags quiz button
    Button(win, text = "Flags", borderwidth = 0, command = flagsModeSelection, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Flags quiz button
    Button(win, text = "Delete account", borderwidth = 0, command = delete, bg = red, fg = white, width = 16, height = 2, font = (font, 12)).pack()
    

    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
    # Logout button
    Button(win, image = logoutIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    

# --- REGISTERING FUNCTIONS ---
def checkPassword():
    regPass = passwordIn.get()
    regConfPass = confPasswordIn.get()

    if regPass != regConfPass:
        messagebox.showerror("Invalid Input!", "Your password and confirmed password must be equal.")

    elif len(regPass) <= 5 or len(regConfPass) <= 5:
        messagebox.showerror("Invalid Input!", "Your password must be over 5 characters.")

    elif regPass == regConfPass and len(regPass) > 5 and len(regConfPass) > 5:
        f = open(f"Accounts/{username}.txt", "a")
        f.write(username + "\n")
        f.write(regPass)
        f.close()

        f = open(f"Highscores/{username}.txt", "a")
        f.write(f"Nothing\n")
        f.write("0")

        login()
        messagebox.showinfo("Password creation successful!", "Now login to your new account.")

    else:
        messagebox.showerror("Invalid Input!", "Invalid Input. Please try again.")

def createPassword():
    # With the 'global' method, variables declared in the function can be used elsewhere
    global passwordIn
    global confPasswordIn

    # Clears the Window by identifying each 'child' on the Window and then destroying it until all of the 'children' have been destroyed
    for widget in win.winfo_children():
        widget.destroy()

    # Title
    Label(win, image = regIcon, text = " Create Password", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Password Creation Input
    Label(win, text = "Create your password:", bg = white, fg = grey, font = (font, 12)).pack()

    passwordIn = Entry(win, fg = grey, bg = lgrey, borderwidth = 0, font = (font, 12))
    passwordIn.pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Password Creation Input
    Label(win, text = "Confirm your password:", bg = white, fg = grey, font = (font, 12)).pack()

    confPasswordIn = Entry(win, fg = grey, bg = lgrey, borderwidth = 0, font = (font, 12))
    confPasswordIn.pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Enter button
    Button(win, image = enterIcon, command = checkPassword, borderwidth = 0, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
    # Back to Home button
    Button(win, image = homeIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)

def createUsername():
    # With the 'global' method, variables declared in the function can be used elsewhere
    global username

    # Takes the first three letters of the variable 'name'
    nameSubstring = name[0:3]

    # Combines the name substring and the age to form the username
    username = nameSubstring + age

    upperUsername = username.upper()
    lowerUsername = username.lower()

    fileExists = exists(f"Accounts/{username}.txt")
    upperFileExists = exists(f"Accounts/{upperUsername}.txt")
    lowerFileExists = exists(f"Accounts/{lowerUsername}.txt")

    if fileExists == False and lowerFileExists == False and upperFileExists == False:

        createPassword()

        # Displays a messagebox to say what the username is
        messagebox.showinfo("Username successfully created!", f"Your username is {username}. Time to create your password!")

    elif fileExists == True or lowerFileExists == True or upperFileExists == True:
        # If an account with these credentials already exists, this error will show
        messagebox.showerror("Invalid Input!", "An account with these details already exists!")

def checkInputs():
    # With the 'global' method, variables declared in the function can be used elsewhere
    global name
    global age

    # Gets the inputs from the entry widget
    name = nameIn.get()
    age = ageIn.get()

    if not name.isalpha():
        messagebox.showerror("Invalid Input!", "Invalid and/or non-existent input for 'first name'.")

    elif not age.isdigit():
        messagebox.showerror("Invalid Input!", "Invalid and/or non-existent input for 'age'.")

    elif name.isalpha() and age.isdigit():

        # Covers the variable 'age' to an integer
        age = int(age)

        if age >= 122:
            messagebox.showerror("Invalid Input!", "Please enter your real age. There's no way you're that old!")

        else:
            # Converts the integer 'age' back into a string
            age = str(age)

            createUsername()

def register():
    # With the 'global' method, variables declared in the function can be used elsewhere
    global nameIn
    global ageIn

    # Clears the Window by identifying each 'child' on the Window and then destroying it
    for widget in win.winfo_children():
        widget.destroy()

    # Title
    Label(win, image = regIcon, text = " Register", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Name Input
    Label(win, text = "Enter your first name:", bg = white, fg = grey, font = (font, 12)).pack()

    nameIn = Entry(win, fg = grey, bg = lgrey, borderwidth = 0, font = (font, 12))
    nameIn.pack()

    # Placeholder
    Label(text="", bg = white, font = (font, 12)).pack()

    # Age Input
    Label(win, text = "Enter your age:", bg = white, fg = grey, font = (font, 12)).pack()

    ageIn = Entry(win, fg = grey, bg = lgrey, borderwidth = 0, font = (font, 12))
    ageIn.pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Enter button
    Button(win, image = enterIcon, command = checkInputs, borderwidth = 0, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
    # Back to Home button
    Button(win, image = welcomeIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


# --- LOGGING IN FUNCTIONS ---
def checkLoginInputs():
    # With the 'global' method, variables declared in the function can be used elsewhere
    global usernameIn

    usernameIn = usernameEn.get()
    passIn = passEn.get()

    logFileExists = exists(f"Accounts/{usernameIn}.txt")

    if logFileExists == False:
        messagebox.showerror("This account does not exist!", "Make sure you typed your username correctly and that the casing for the letters is correct.")

    elif logFileExists == True:
        f = open(f"Accounts/{usernameIn}.txt", "r")
        line = f.readlines()
        checkPassIn = line[1]
        f.close()

        if checkPassIn != passIn:
            messagebox.showerror("Incorrect Password!", "The password that you entered is not correct.")

        elif checkPassIn == passIn:
            dashboard()
            
            messagebox.showinfo("Login successful!", "Your login was successful")

def login():
    # With the 'global' method, variables declared in the function can be used elsewhere
    global usernameEn
    global passEn

    # Clears the Window by identify each 'child' on the Window and then destroying it
    for widget in win.winfo_children():
        widget.destroy()

    # Title
    Label(win, image = loginIcon, text = " Login", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Name Input
    Label(win, text = "Enter your username:", bg = white, fg = grey, font = (font, 12)).pack()

    usernameEn = Entry(win, fg = grey, bg = lgrey, borderwidth = 0, font = (font, 12))
    usernameEn.pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Name Input
    Label(win, text = "Enter your password:", bg = white, fg = grey, font = (font, 12)).pack()

    passEn = Entry(win, fg = grey, bg = lgrey, borderwidth = 0, font = (font, 12))
    passEn.pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Enter button
    Button(win, image = enterIcon, command = checkLoginInputs, borderwidth = 0, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack()


    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)
    
    # Back to Home button
    Button(win, image = welcomeIcon, borderwidth = 0, command = main, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


# --- MAIN FUNCTION ---
def main():
    # Clears the Window by identify each 'child' on the Window and then destroying it
    for widget in win.winfo_children():
        widget.destroy()

    # Title
    Label(win, image = welcomeIcon, text = " Welcome", compound = LEFT, bg = grey, fg = white, width = 2560, height = 120, font = (font, 24)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Login button
    Button(win, text = " Login", borderwidth = 0, command = login, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()

    # A placeholder
    Label(win, text = "", bg = white).pack()

    # Register button
    Button(win, text = " Register", borderwidth = 0, command = register, bg = grey, fg = white, width = 16, height = 2, font = (font, 12)).pack()
    

    # Exit button
    Button(win, image = exitIcon, borderwidth = 0, command = exit, compound = LEFT, bg = grey, fg = white, width = 65, height = 65).pack(side = BOTTOM, anchor = NW)


    # Refreshes the window at a set rate (usually 60 times per second (60 FPS))
    win.mainloop()


main()