import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()

root.geometry("600x400")
# root.resizable(False, False)
root.title("Widgets Examples")


image = Image.open("StarkIndustries.png")
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root, image=photo, padding=5)
label.config(font=("Seoge UI",20))
label.pack()



root.mainloop()

