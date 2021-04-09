from tkinter import *
from tkinter.ttk import *
textContent = ""
fileName = ""
window = Tk()

text = StringVar()
fileName = text.get()
newLabel = Label(window, text="Enter file name(with extension): ")
newLabel.grid(row=0, column=0)

newLabelText = Entry(window, width=20, textvariable=text)
newLabelText.grid(row=0, column=1)
newLabelText.focus()

okButton = Button(window, text="Ok", command=window.destroy)
okButton.grid()
window.mainloop()

fileName = text.get()
print(fileName)

window1 = Tk()
textField = Text(window1, height=44, width=168)
textField.grid(row=0, column=0)

scrollBar = Scrollbar(window1, orient="vertical", command=textField.yview)
scrollBar.grid(row=0, column=1,sticky="ns")
textField["yscrollcommand"] = scrollBar.set
textContent = textField.get("1.0", "end")

window1.mainloop()

file = open(fileName, "w")
file.write(textContent)
file.close()
print(textContent)