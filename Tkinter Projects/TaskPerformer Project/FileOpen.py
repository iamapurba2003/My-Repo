from tkinter import *
from tkinter.ttk import *
from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog as fd
import os


def main():
    Open = Tk()
    Open.geometry('200x200')
    # def main():
    fileTypes = (
    ('All Files', '*.*'),
    )

    filename = fd.askopenfilenames(title= 'Open a File', initialdir = '/', filetypes=fileTypes)
    for items in filename:
        os.startfile(items)

    Open.destroy()
    Open.mainloop()