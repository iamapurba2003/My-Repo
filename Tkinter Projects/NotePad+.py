from tkinter import *
import datetime as dt
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import webbrowser

# A new window with text field and other attributes
base = Tk()

# Tkinter window configurations
base.geometry('500x300')
base.minsize(200,200)
base.iconbitmap("D:/Documents/Git Folder/Tkinter Projects/NotePad+.ico")
fileName = 'Untitled'
base.title(f"{fileName} - NotePad+")


# Text Field
textField = Text(base, height=10, width=13)
textField.pack(side='left', fill=BOTH, expand=True)


def saveasFile(event='<Control-S>'):
    dateandtime = dt.datetime.now()
    global fileName
    file = fd.asksaveasfile(initialfile=fileName, defaultextension=".txt",filetypes=[("All Files", "*.*"), ("Text File","*.txt"), ('Python Source File','*.py'), ('JavaScript Source File', '*.js'), ('TypeScript Source File', '*.ts'), ('C Source File', '*.c'), ('C++ Source File', '*.cpp'), ('HTML Document', '*.html'), ('Java Source File', '*.java'), ('CascadingStyleSheet Source File', '*.css'), ('Windows Batch File', '*.bat'), ('Windows PowerShell Profile', '*.ps1')], confirmoverwrite = True
    )
    with open(file.name, 'a') as f:
        f.write(textField.get('1.0', 'end'))
        f.close()
    
    fileName = file.name
    base.title(f"{file.name} -- NotePad+ -- Saved @ {dateandtime.strftime('%H:%M:%S')}")


def saveFile(event='<Control-s>'):
    dateandtime = dt.datetime.now()
    global fileName
    if fileName == 'Untitled':
        file = fd.asksaveasfile(initialfile = fileName, defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text File","*.txt"), ('Python Source File','*.py'), ('JavaScript Source File', '*.js'), ('TypeScript Source File', '*.ts'), ('C Source File', '*.c'), ('C++ Source File', '*.cpp'), ('HTML Document', '*.html'), ('Java Source File', '*.java'), ('CascadingStyleSheet Source File', '*.css'), ('Windows Batch File', '*.bat'), ('Windows PowerShell Profile', '*.ps1')])
        
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


def openFile(event='<Control-o>'):
    global fileName
    fileOpen = fd.askopenfile()
    mainFile = open(fileOpen.name,'r')
    fileRead = mainFile.read()
    textField.insert(INSERT, f'{fileRead}')
    fileName = fileOpen.name.split('/')
    base.title(f'Opened: \'{fileName[-1]}\' -- NotePad+')


def about(event=None):
    def callback():
        webbrowser.open_new("https://github.com/Himangshu-De/My-Repo/tree/master/Tkinter%20Projects")

    
    if mb.askyesno('About','NotePad+ is an Open Source Program by Himangshu De, its development files are on GitHub\nDo you want to visit?') == True:
        callback()
    

def quit(event='<Control-q>'):
    base.quit()


# Menu widget attributes
menubar = Menu(base)
fileMenu = Menu(menubar, tearoff=0)

fileMenu.add_command(label='Save         Ctrl+S', command=saveFile)
fileMenu.add_command(label='Save As    Ctrl+Shift+S', command=saveasFile)
fileMenu.add_command(label='Open        Ctrl+O', command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit           Ctrl+Q', command=quit)


menubar.add_cascade(label='File', menu=fileMenu)
menubar.add_cascade(label='About', command=about)


scrollBar = Scrollbar(base, orient="vertical", command=textField.yview)
scrollBar.pack(side='right', fill=Y)
textField["yscrollcommand"] = scrollBar.set

base.config(menu=menubar)

# Binding Keyboard combos
base.bind('<Control-s>',saveFile)
base.bind('<Control-S>',saveasFile)
base.bind('<Control-o>',openFile)
base.bind('<Control-q>',quit)

# Running the main tkinter window
base.mainloop()
