from threading import Thread
import threading
from tkinter import filedialog
from tkinter import *
import compression


def create_inter():
    global is_backup
    is_backup = False
    global root
    root = Tk()
    global win_width, win_height, scr_width, scr_height, center_x, center_y
    win_width = 600
    win_height = 400
    scr_width = root.winfo_screenwidth()
    scr_height = root.winfo_screenheight()
    center_x = int(scr_width / 2 - win_width / 2)
    center_y = int(scr_height / 2 - win_height / 2)
    global eve
    eve = threading.Event()
    global path
    path = ""
    global t
    t = Thread(target=check_folder)
    global b_list
    b_list = []
    root.title("back up your files")
    root.iconbitmap('assets/cloud.ico')
    root.configure(width=win_width, height=win_height)
    root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
    button_text = "Select a folder"
    button_x = 100
    button_y = 100
    button(button_text, button_x, button_y)
    root.mainloop()


def get_path():
    return path


def backup_folder():
    compression.compressfile(path, "test")


def check_folder():
    global is_backup
    is_backup = True
    while not eve.is_set():
        continue
    if 'lbl' in globals():
        text = "Selected directory:" + path
        lbl.config(text=text)
    else:
        text = "Selected Directory: " + path
        label_set(text)
        button_text = "backup"
        button_x = 150
        button_y = 40
        button(button_text, button_x, button_y)


def label_set(text: str):
    print("got here")
    global lbl
    lbl = Label(root, text=text)
    lbl.pack()
    root.update()


def select_folder():
    eve.clear()
    t = Thread(target=check_folder)
    t.start()
    global path
    path = ""
    path = filedialog.askdirectory()
    print(path)
    eve.set()


def button(button_text: str, button_x: int, button_y: int):
    button_height = 1
    button_width = 10
    if 'is_backup' in globals():
        if not is_backup:
            b = Button(root, text=button_text, command=select_folder, width=button_width, height=button_height)
        else:
            b = Button(root, text=button_text, command=backup_folder, width=button_width, height=button_height)
    else:
        b = Button(root, text=button_text, command=select_folder, width=button_width, height=button_height)
    b_list.append(b)
    b.pack()
    root.update()
    print("hello")
    return


create_inter()
