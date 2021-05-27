from tkinter import *
from tkinter.ttk import *
import webbrowser as web

def mainFunc():
    new = Tk()
    new.geometry('300x250')
    new.title('Web Search')

    def opener(event='<Return>'):
        main = keyword.get('1.0','end')
        keyword.delete('1.0','end')
        link = 'https://www.google.com/search?q={}'.format(main)
        web.open_new(link)
        Label(new, text='Opening on Web').place(x = 100, y=70)


    Label(new, text='Enter searchword: ').place(y=1)
    keyword = Text(new, width=25, height=1, font=('Segoe UI', 11))
    keyword.place(x= 0, y=30)
    keyword.bind('<Return>', opener)
    keyword.focus()

    Button(new, text="Go!",command=opener).place(y=70)
    new.mainloop()