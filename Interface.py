import threading
from tkinter import filedialog
from tkinter import *
import tkinter
import tkinter.messagebox

eve = threading.Event
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
    eve.set
    print(path)


def button(top):
    B = tkinter.Button(top, text="select a folder", command=select_folder, width=10, height=1)
    while not eve.is_set:
        continue
    print("ee")
    B.pack()


def interface():
    root.withdraw()
    top = tkinter.Tk()
    button(top)
    print(path)
    top.mainloop()
interface()