import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


root = tk.Tk()
greetings=tk.StringVar()
root.geometry("600x400")
# root.resizable(False, False)
root.title("Widgets Examples")

text= tk.Text(root, height=900, width= 168)
text.grid(row=0,column=0,sticky="ew")

text.insert("1.0","Please enter a comment")

textScroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
textScroll.grid(row=0,column=1,sticky="ns")
text["yscrollcommand"]= textScroll.set


root.mainloop()