import py7zr
import shutil


def copy_folder(src_folder: str):
    dst_folder = "C:/Users/Aviv Avichail/PycharmProjects/BackUp_Project/tmp/backup_folders"
    shutil.copytree(src_folder, dst_folder)
    return dst_folder

def compressfile(filepath: str, archname: str):
    archpath = "C:\\Users\\Aviv Avichail\\PycharmProjects\\BackUp_Project\\" + archname + ".7z"
    with py7zr.SevenZipFile(archpath,'w') as archive:
        archive.writeall(filepath)
        return archpath

def extract_file(filepath : str):
    with py7zr.SevenZipFile(filepath, 'r') as archive:
        archive.extractall(path="C:\\Users\\Aviv Avichail\\PycharmProjects\\BackUp_Project\\tmp")