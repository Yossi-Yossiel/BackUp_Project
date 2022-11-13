import os
import threading
from tkinter import filedialog
from tkinter import *

eve = threading.Event()
root = Tk()
path = ""


def label_set(text: str):
    lbl = Label(root, text=text, relief=RAISED)
    lbl.pack
    root.mainloop()


def select_folder():
    global path
    path = ""
    path = filedialog.askdirectory()
    var = "selected directory: " + str(path)
    print(var)
    eve.set
    print(path)


def button(top):
    B = Button(top, text="select a folder", command=select_folder, width=10, height=1)
    B.pack()
    print("hello")



def interface():
    root.withdraw()
    top = Tk()
    button(top)
    top.mainloop()
    while not eve.is_set():
        continue
    return path