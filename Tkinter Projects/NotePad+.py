from tkinter import *
from tkinter.ttk import *
import datetime as dt
from tkinter import filedialog as fd


# A new window with text field and other attributes
base = Tk()

base.geometry('500x300')
base.minsize(200,200)
base.iconbitmap("C:/Users/Himangshu De/Documents/Media and Others/Git Folder/Tkinter Projects/NotePad+.ico")

fileName = 'Untitled'

base.title(f"{fileName} - NotePad+")
textField = Text(base, height=10, width=13)
textField.pack(side='left', fill=BOTH, expand=True)


def saveasFile(event='<Return>'):
    dateandtime = dt.datetime.now()
    global fileName
    file = fd.asksaveasfile(initialfile=fileName, defaultextension="*.txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt"), ('Python File',"*.py")], confirmoverwrite = True
    )
    with open(file.name, 'a') as f:
        f.write(textField.get('1.0', 'end'))
        f.close()
    
    fileName = file.name
    base.title(f"{file.name} -- NotePad+ -- Saved @ {dateandtime.strftime('%H:%M:%S')}")


def saveFile():
    dateandtime = dt.datetime.now()
    global fileName
    if fileName == 'Untitled':
        file = fd.asksaveasfile(initialfile = fileName, defaultextension='*.txt', filetypes=[("All Files", "*.*"), ("Text File","*.*"), ('Python Source File','*.py'), ('JavaScript Source File', '*.js'), ('TypeScript Source File', '*.ts'), ('C Source File', '*.c'), ('C++ Source File', '*.cpp'), ('HTML Document', '*.html'), ('Java Source File', '*.java'), ('CascadingStyleSheet Source File', '*.css'), ('Windows Batch File', '*.bat'), ('Windows PowerShell Profile', '*.ps1')])
        
        f = open(file.name, 'w')
        f.write(textField.get('1.0', END))
        f.close()
        fileName = file.name
        base.title(f"{file.name} -- NotePad+ -- Saved @ {dateandtime.strftime('%H:%M:%S')}")
    
    else:
        f = open(fileName, 'w')
        f.write(textField.get('1.0', END))
        f.close()
        base.title(f"{fileName} -- NotePad+ -- Saved @ {dateandtime.strftime('%H:%M:%S')}")


def openFile():
    global fileName
    fileOpen = fd.askopenfile()
    mainFile = open(fileOpen.name,'r')
    fileRead = mainFile.read()
    textField.insert(INSERT, f'{fileRead}')
    fileName = fileOpen.name
    base.title(f'Opened: \'{fileName}\' -- NotePad+')


menubar = Menu(base)
fileMenu = Menu(menubar, tearoff=0)
HelpMenu = Menu(menubar, tearoff=0)

fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_command(label='Save As', command=saveasFile)
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=base.quit)

HelpMenu.add_command(label='Help')

menubar.add_cascade(label='File', menu=fileMenu)
menubar.add_cascade(label='Help', menu=HelpMenu)


scrollBar = Scrollbar(base, orient="vertical", command=textField.yview)
scrollBar.pack(side='right', fill=Y)
textField["yscrollcommand"] = scrollBar.set

base.config(menu=menubar)

base.mainloop()
