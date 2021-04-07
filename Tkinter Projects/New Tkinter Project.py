from tkinter import * 
from tkinter.ttk import *

def save():
    with open("C:/Users/Himangshu De/Documents/newFile.txt", "a") as r:
        r.write(textContent)
        r.close()
        
window = Tk()
frame = Frame(window)
frame.pack(side="top")
window.geometry("600x400")
window.title("Notepad")
SaveButton = Button(frame,text="Save", command=save)
SaveButton.pack()

textField = Text(window, height=500, width=600)
textField.pack(side="bottom")
textContent = textField.get("1.0", "end")
window.mainloop()




