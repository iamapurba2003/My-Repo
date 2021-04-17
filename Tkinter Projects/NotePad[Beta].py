from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("FileName")
text = StringVar()

newLabel = Label(window, text="Enter file name(with extension): ")
newLabel.grid(row=0, column=0)

newLabelText = Entry(window, width=20, textvariable=text)
newLabelText.grid(row=0, column=1)
newLabelText.focus()

okButton = Button(window, text="Ok", command=window.destroy)
okButton.grid()
window.mainloop()
fileName = text.get()

window1 = Tk()
window1.title(fileName)

textField = Text(window1, height=44, width=168)
textField.grid(row=1, column=0)

def save():
    file = open(fileName, "w")
    file.write(textField.get("1.0", "end"))
    file.close()


saveButton = Button(window1, text="Save", command=save)
saveButton.grid(row=0, column=0)
scrollBar = Scrollbar(window1, orient="vertical", command=textField.yview)
scrollBar.grid(row=1, column=1,sticky="ns")
textField["yscrollcommand"] = scrollBar.set


window1.mainloop()
