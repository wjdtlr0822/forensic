import tkinter
from tkinter import filedialog

def fileselect():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(parent=root,initialdir="/",title='Please select a directory')
    print("read file path : ",file_path)
    return file_path