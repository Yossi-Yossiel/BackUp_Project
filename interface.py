from tkinter import filedialog
from tkinter import *
import tkinter
import tkinter.messagebox

path = ""

def select_folder():
    path = ""
    path = filedialog.askdirectory()
    var = "selected directory: " + str(path)
    lbl = Label(root, textvariable=var, relief=RAISED)
    return path
    print(path)


def button():
    B = tkinter.Button(top, text="select a folder", command=select_folder, width=10, height=1)
    print(B)
    print("returned")
    B.pack()


root = Tk()
root.withdraw()
top = tkinter.Tk()

button()

top.mainloop()