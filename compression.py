import py7zr


def compressfile(filepath: str, archname: str):
    archpath = "C:\\Users\\Aviv Avichail\\PycharmProjects\\BackUp_Project\\" + archname + ".7z"
    with py7zr.SevenZipFile(archpath,'w') as archive:
        archive.writeall(filepath)
        return archpath

def extractfile(filepath : str):
    with py7zr.SevenZipFile(filepath, 'r') as archive:

        archive.extractall(path="C:\\Users\\Aviv Avichail\\PycharmProjects\\BackUp_Project\\tmp")
