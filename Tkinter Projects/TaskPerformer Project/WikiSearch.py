from tkinter import *
from tkinter.ttk import *
import pywhatkit as kit
import tkinter.messagebox as mb

def main():
    source = Tk()
    source.title('WikiSearch')
    source.geometry('270x75')

    def infosearch(event='<Return>'):
        try:
            n = str(kit.info(wikiSearch.get('1.0','end')))
            mb.showinfo(title='About '+wikiSearch.get('1.0', 'end'), message=n)
            wikiSearch.delete('1.0','end')
        except Exception as e:
            mb.showerror('Not Found!', message=e)
            wikiSearch.delete('1.0','end')


    Label(source, text='Enter search word: ').place(x=0, y=0)
    wikiSearch = Text(source, width=20, height=1)
    wikiSearch.place(x=0,y=20)
    wikiSearch.focus()
    wikiSearch.bind('<Return>', infosearch)
    Button(source, text='Search!', command=infosearch).place(x=175, y=19)
    source.mainloop()