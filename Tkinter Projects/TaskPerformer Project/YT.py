from tkinter import *
from tkinter.ttk import *
import pywhatkit as kit

def main():
    new =Tk()
    new.title('Play on YouTube')
    new.geometry('250x75')
    Label(new, text='Enter keyword: ').place(y=1, anchor='nw')

    keyword = Text(new, width=20, height=1)
    keyword.place(x=80, anchor='nw')
    keyword.focus()

    def player():
        main = keyword.get('1.0','end')
        kit.playonyt(main)
        keyword.delete('1.0','end')
        Label(new, text='Opening on YouTube').place(x = 80, y=30)
    Button(new, text="Go!",command=player).place(y=30)
    new.mainloop()  
