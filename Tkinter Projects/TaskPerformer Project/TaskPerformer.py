from tkinter import *
from tkinter.ttk import *
import pywhatkit as kit
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import os
import WA
import YT
window = Tk()
window.update()
str1 = StringVar()

storer = ''

def commands():
    
    # For Sending a WA Message
    if str1.get() == 'Send a WA Message':
        WA.main()

    # For playing content on YouTube
    if str1.get() == 'Play on YouTube':
        YT.main()
    
    # For a Web Search
    elif str1.get() == 'Search on Web':
        new = Tk()
        Label(new, text='Enter searchword: ').place(y=1, anchor='nw')
        keyword = Text(new, width=40, height=1, font=('Segoe UI', 11))
        keyword.place(x=80, anchor='nw')
        keyword.focus()
        
        def opener():
            main = keyword.get('1.0','end')
            kit.search(main)
            Label(new, text='Searching on Web').place(x = 80, y=30)
        
        Button(new, text="Go!",command=opener).place(y=30)
        new.mainloop()

    # Search on Wikipedia
    elif str1.get() == 'Search on Wikipedia':
        source = Tk()
        Label(source, text='Enter search word: ').place(x=0, y=0)
        wikiSearch = Text(source, width=20, height=1)
        wikiSearch.place(x=0,y=20)
        wikiSearch.focus()
        def infosearch():
            try:
                n = str(kit.info(wikiSearch.get('1.0','end')))
                mb.showinfo(title='About '+wikiSearch.get('1.0', 'end'), message=n)
            except Exception as e:
                mb.showerror('Not Found!', message=e)

        Button(source, text='Search!', command=infosearch).place(x=20, y=70)


        source.mainloop()

    # Open Files on this Computer
    elif str1.get() == 'Open files on this computer':
        Open = Tk()
        Open.geometry('200x200')
        # def main():
        fileTypes = (
        ('All Files', '*.*'),
        ('Text Files', '*.txt'),
        ('Python Files', '*.py')
        )

        filename = fd.askopenfilenames(title= 'Open a File', initialdir = '/', filetypes=fileTypes)
        for items in filename:
            os.startfile(items)

        Open.destroy()
        Open.mainloop()
    
    # Shut down the System
    elif str1.get() == 'Shut Down the system':
        print('hi4')
    
    # Open a web link
    elif str1.get() == 'Open any web link':
        print('hi5')
    
    # Send an Email
    elif str1.get() == 'Send an Email':
        print('hi6')

    elif str1.get() == '<Select>':
        pass
    else:
        pass



combo = Combobox(window, textvariable=str1, width=25)
combo['values'] = (
    '<Select>',
    'Send a WA Message',
    'Play on YouTube',
    'Search on Web',
    'Search on Wikipedia',
    'Open files on this computer',
    'Shut Down the system', 
    'Open any web link',
    'Send an Email'
)
combo['state'] = 'readonly'
combo.current(0)
combo.place(x=10, y=10, anchor='nw')
window.update()

okButton =Button(window, text="Ok", command=commands)
okButton.place(x=10, y=60, anchor='nw')
window.update()

okButton =Button(window, text="Quit", command=window.destroy)
okButton.place(x=90, y=60, anchor='nw')
window.update()

window.mainloop()
