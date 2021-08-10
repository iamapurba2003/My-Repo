from tkinter import *
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
import pickle

# !======== Code for a Tkinter Window ==========!
app = Tk()
app.wm_title("File Reader")
# app.geometry("500x300")

mainFrame = Frame(app)
mainFrame.pack(side=TOP, anchor=N, expand=True, fill=X)

textField = ScrolledText(app, height=30, width=20)
textField.pack(side=BOTTOM, anchor=S, fill=X)
textField.insert(1.0, "You can't type here anything!...")
textField['state'] = 'disabled'

# !========= Function For File operations ============!
def FileOpen(event = "None"):
    fileName = fd.askopenfile(mode="r")
    if ".txt" not in fileName.name:
        mainFile = open(fileName.name,"rb")
        reader = pickle.load(mainFile)

    else:
        mainFile = open(fileName.name,"r")
        reader = mainFile.read()

    if textField.get(1.0, END) == "":
        textField['state'] = 'normal'
        textField.insert(1.0, reader)
        textField['state'] = 'disabled'

    if textField.get(1.0, END) != "":
        textField['state'] = 'normal'
        textField.delete(1.0, END)
        textField.insert(1.0, reader)
        textField['state'] = 'disabled'

    

openPrompt = Button(mainFrame, text="Open File",command=FileOpen)
openPrompt.pack(side=TOP, anchor=N)

LabelMain = Label(mainFrame, text="File opened will be processed and its content will be shown")
LabelMain.pack(side=TOP, anchor=N)

app.mainloop()