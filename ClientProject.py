import os
import shutil
import socket
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import filedialog
import py7zr


def send_file(filepath:str):
    client_socket.connect(server_tup)
    client_socket.send()


def check_backup_button():
    while True:
        if backup_event:
            break
        continue
    start_compress(arch_path, archive_name)


def copy_folder(src_folder: str):
    print(src_folder)
    for i in range(10):
        dst_folder = f"C:/Users/Aviv Avichail/PycharmProjects/BackUp_Project/tmp/backup_folders/{i}"
        if not os.path.exists(dst_folder):
            global archive_name
            archive_name = f"{archive_name}{i}"
            break
    shutil.copytree(src_folder, dst_folder)
    index = dst_folder.find("/tmp")
    return f".{dst_folder[index::]}"


def backup_folder():
    print("dodush")
    global arch_path
    arch_path = copy_folder(path)
    backup_event.set()
    global t2
    t2 = threading.Thread(target=check_backup_button)
    t2.start()


def check_folder():
    global is_backup
    is_backup = True
    while not eve.is_set():
        continue
    if 'lbl' in globals():
        text = "Selected directory:" + path
        lbl.config(text=text)
        button_text = "backup"
        button(button_text)


def select_folder():
    eve.clear()
    global t
    t = Thread(target=check_folder)
    t.start()
    global path
    path = ""
    path = filedialog.askdirectory()
    print(path)
    eve.set()


def button(button_text: str):
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


def start_compress(filepath: str, arch_name: str):
    sevenzip_filepath = "C:\\Users\\Aviv Avichail\\PycharmProjects\\BackUp_Project\\tmp\\backup_folders\\" +\
                        arch_name + ".7z"
    t3 = threading.Thread(target=compress_folder, args=(sevenzip_filepath,filepath))
    t3.run()


def compress_folder(sevenzip_filepath: str, filepath: str):
    print("start")
    with py7zr.SevenZipFile(sevenzip_filepath, 'w') as archive:
        archive.writeall(filepath)
        send_file(sevenzip_filepath)
        return arch_path



def extract_file(filepath: str):
    with py7zr.SevenZipFile(filepath, 'r') as archive:
        archive.extractall(path="C:\\Users\\Aviv Avichail\\PycharmProjects\\BackUp_Project\\tmp")


def delete_tmp_folders():
    folder = "C:/Users/Aviv Avichail/PycharmProjects/BackUp_Project/tmp/backup_folders"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def create_inter():
    root.title("back up your files")
    root.iconbitmap('assets/cloud.ico')
    root.configure(width=win_width, height=win_height)
    root.geometry(f'{win_width}x{win_height}+{center_x}+{center_y}')
    button_text = "Select a folder"
    button(button_text)
    lbl.pack()
    root.mainloop()


server_tup = ("127.0.0.1", 5000)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
archive_name = "test"
arch_path = ""
backup_event = threading.Event()
t2 = threading.Thread(target=check_backup_button)
is_backup = False
root = Tk()
lbl = Label(root, text="Selected directory:")
win_width = 600
win_height = 400
scr_width = root.winfo_screenwidth()
scr_height = root.winfo_screenheight()
center_x = int(scr_width / 2 - win_width / 2)
center_y = int(scr_height / 2 - win_height / 2)
eve = threading.Event()
path = ""
t = Thread(target=check_folder)
b_list = []
t2.start()
delete_tmp_folders()
create_inter()
