from tkinter import *
import datetime as dt
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter.font 
from tkinter.scrolledtext import ScrolledText
import webbrowser
import platform

# A new window with text field and other attributes
base = Tk()
Store = "0"
Size = 0
# Tkinter window configurations
base.geometry('500x300')
base.minsize(200,200)
if platform.system() == "Linux":
    mainImage = PhotoImage(file="./NotePad+ png images/NotePad0.png")
    base.tk.call('wm', 'iconphoto', base._w, mainImage)

if platform.system() == "Windows":
    base.iconbitmap("./NotePad+ png images/NotePad0.png")
fileName = 'Untitled'
base.title(f"{fileName} - NotePad+")

Store = StringVar()
status = 0

# Text Field
textField = ScrolledText(base, height=1, width=2,font=('Arial',16))
textField.pack(anchor=N, fill=BOTH, expand=True)
textField.config(wrap='none')
textField.focus()

#ScrollBars
scrollBar = Scrollbar(base, orient="horizontal", command=textField.xview)
scrollBar.pack(side=BOTTOM, anchor=S, fill=X)
textField["xscrollcommand"] = scrollBar.set


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


def checker(event="none"):
    global fileName
    base.title(f"{fileName[-1]}* -- NotePad+")

def openFile(event='<Control-o>'):
    global fileName
    fileOpen = fd.askopenfile()
    mainFile = open(fileOpen.name,'r')
    fileRead = mainFile.read()
    if textField.get != "":
        textField.delete(1.0, END)
        textField.insert(1.0, f'{fileRead}')
    else:
        textField.insert(1.0, fileRead)
    fileName = fileOpen.name.split('/')
    base.title(f'Opened: \'{fileName[-1]}\' -- NotePad+')
    textField.bind("<Key>", checker)


def about(event=None):
    def callback():
        webbrowser.open_new("https://github.com/Himangshu-De/My-Repo/tree/master/Tkinter%20Projects")

    okcancel = mb.askyesno('About','NotePad+ is an Open Source Program by Himangshu De, its development files are on GitHub\nDo you want to visit?')
    if okcancel == True:
        callback()
    

def dark():
    global status
    _status = status
    if _status == 1:
        textField.config(bg='white', fg='black', insertbackground='black')
        menubar.config(bg="orange", fg="black")
        status=0

    if _status == 0:
        textField.config(bg='black', fg='yellow', insertbackground='yellow')
        menubar.config(bg="grey", fg="yellow")
        status = 1
        

def font():
    app = Toplevel()
    # app.geometry("410x340")
    app.resizable(False, False)
    app.attributes("-topmost", 1)
    Value =12
    Name = "Arial"
    # _theme = theme
    # Function Defs
    def Mode():
        # nonlocal _theme
        if status==1:
            app.config(background='#4a4a4a')
            FontFamList.config(bg="#828282", fg="yellow")
            FontFamLabel.config(fg='yellow', bg="#4a4a4a")
            FontSizeLabel.config(fg="yellow",bg="#4a4a4a")
            FontSizeList.config(fg='yellow', bg='#828282')
            okButton.config(bg="#4a4a4a", fg='yellow')
            SampleFrame.config(bg="#4a4a4a",fg="yellow")
            LabelText.config(bg="#4a4a4a", fg="yellow")
            FontFamFrame.config(bg="#4a4a4a")
            FontSizeFrame.config(bg="#4a4a4a")
        
        if status == 0:
            app.config(background='white')
            FontFamList.config(bg="white", fg="black")
            FontFamLabel.config(fg='black', bg="white")
            FontSizeLabel.config(fg="black",bg="white")
            FontSizeList.config(fg='black', bg='white')
            okButton.config(bg="white", fg="black")
            SampleFrame.config(bg="white",fg="black")
            LabelText.config(bg="white", fg="black")
            FontFamFrame.config(bg="white")
            FontSizeFrame.config(bg="white")
        
        

    def updater(name, size):
        nonlocal Value, Name
        LabelText.config(font=(f'{name}', size))
        Value, Name = size, name
        return Value, Name
        
    def save():
        nonlocal Value, Name
        textField.config(font=(Name, Value))
        app.destroy()

    def FontGet(event="None"):
        # For size & Family
        nonlocal Value, Name
        siz = FontSizeList.curselection()
        fam = FontFamList.curselection()
        for i in siz:
            Value = FontSizeList.get(i)

        for i in fam:
            Name = FontFamList.get(i)

        updater(name=Name, size=int(Value))
        

    SampleFrame = LabelFrame(app, text="Sample", height=30, width=30)
    SampleFrame.pack(side=TOP, anchor=NW, fill=X)


    names=list(tkinter.font.families(app))
    FontFamVals = StringVar(value=tuple(names))
    FontSizeVals= StringVar(value=tuple([8,9,10,11,12,14,16,18,20,22,24,26,28,36,48,72]))

    FontFamFrame = Frame(app)
    FontFamFrame.pack(side=LEFT, anchor=N)

    FontFamLabel = Label(FontFamFrame, text="Font Family:")
    FontFamLabel.pack(anchor=NW)



    # Config/Attrib for Font Family Frame and Widgets

    FontFamScrl = Scrollbar(FontFamFrame, orient=VERTICAL)
    FontFamScrl.pack(side=RIGHT, fill=Y)

    FontFamList = Listbox(FontFamFrame, listvariable=FontFamVals, height=10, exportselection=False,width=35)
    FontFamList.pack(anchor=W)
    FontFamList.bind("<<ListboxSelect>>", FontGet)
    FontFamList.config(yscrollcommand=FontFamScrl.set)
    FontFamScrl.config(command=FontFamList.yview)


    # Config/Attrib for Font Size Frame and Widgets
    FontSizeFrame = Frame(app)
    FontSizeFrame.pack(side=RIGHT, anchor=N)
    FontSizeLabel = Label(FontSizeFrame, text="Font Size:")
    FontSizeLabel.pack(side=TOP, anchor=NW)

    FontSizeList =  Listbox(FontSizeFrame, listvariable=FontSizeVals, height=10, exportselection=False)
    FontSizeList.pack(side=LEFT, anchor=W)
    FontSizeList.bind("<<ListboxSelect>>", FontGet)

    FontSizeScrl = Scrollbar(FontSizeFrame, orient=VERTICAL)
    FontSizeScrl.pack(side=RIGHT, fill=Y)
    FontSizeList.config(yscrollcommand=FontSizeScrl.set)
    FontSizeScrl.config(command=FontSizeList.yview)



    LabelText = Label(SampleFrame, text="Sample Text", font=("Arial", 12))
    LabelText.pack()
    okButton = Button(app, text="OK", command=save)
    okButton.pack(anchor=S, side=BOTTOM)
    Mode()
    
    app.mainloop()


def onClose(event="none"):
    if textField.get(1.0, END) != "\n":
        message = mb.askyesnocancel("Exit", "Do you want to save this file and QUIT?")
        if message==True:
            saveasFile()
            base.destroy()
        if message==False:
            base.destroy()
    else:
        base.destroy()


def lengthWord():
    texts = textField.get(1.0,END)
    listMain = texts.split()
    mainLength = len(listMain[-1])
    return str(mainLength+1)

def lastwrdDel(event="None"):
    c = lengthWord()
    del1 = "end-"+c+"c"
    textField.delete(del1,END)


# Menu widget attributes
menubar = Menu(base, background='orange', foreground='black')
fileMenu = Menu(menubar, tearoff=0, background="#b0b0b0", foreground="black")
themeMenu = Menu(menubar,tearoff=0)
fontMenu = Menu(menubar, tearoff=0, bg="#b0b0b0", fg="black")
# Menu Bar File Option Attribs.
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Save         Ctrl+S', command=saveFile)
fileMenu.add_command(label='Save As    Ctrl+Shift+S', command=saveasFile)
fileMenu.add_command(label='Open        Ctrl+O', command=openFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit           Ctrl+Q', command=onClose)

# Menu Bar Theme Option Attribs.
menubar.add_command(label="Theme", command=dark)

fontMenu.add_command(label="Font", command=font)
menubar.add_cascade(label='Format', menu=fontMenu)

menubar.add_cascade(label='About', command=about)



base.config(menu=menubar)

# Binding Keyboard combos
base.bind('<Control-s>',saveFile)
base.bind('<Control-S>',saveasFile)
base.bind('<Control-o>',openFile)
base.bind('<Control-q>',onClose)
base.bind('<Control-T>', dark)
# base.bind('<Key>', auto)
textField.bind('<Control-BackSpace>', lastwrdDel)
base.protocol("WM_DELETE_WINDOW", onClose)
# Running the main tkinter window
base.mainloop()
