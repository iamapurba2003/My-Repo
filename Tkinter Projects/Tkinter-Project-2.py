import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()

root.geometry("600x400")
# root.resizable(False, False)
root.maxsize(600,500)
root.title("Widgets Examples")


image = Image.open("D:/StarkIndustries.jpg")
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root, image=photo, padding=5)
label.config(font=("Seoge UI",20))
label.pack()



root.mainloop()

