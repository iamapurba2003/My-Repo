from tkinter import * 
from tkinter.ttk import *
from PIL import Image, ImageTk

address = input("Enter image address: ")


window = Tk()
window.geometry("1366x768")
window.resizable(True, True)

photo = Image.open(address).resize((1280, 720))
photoLoader = ImageTk.PhotoImage(photo)

newLabel = Label(window, image=photoLoader, text="Image with text", compound="right")
newLabel.pack()

window.mainloop()
