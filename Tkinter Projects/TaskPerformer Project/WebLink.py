from tkinter import *
from tkinter.ttk import *
import webbrowser as wb
def main():
    webOpen = Tk()
    webOpen.title('Browse a Link')
    webOpen.geometry('200x200')
    Label(webOpen, text='Enter the Link:').place(x=0,y=0)

    def executer(event='<Return>'):
        Message(webOpen, text=f"Opening {searchword.get('1.0','end')} on web").place(x=30,y=100)
        org = searchword.get('1.0','end')
        wb.open_new_tab(org)
        searchword.delete('1.0','end')


    searchword = Text(webOpen, width=25,height=1)
    searchword.place(x=0,y=20)
    searchword.bind('<Return>', executer)

    Button(webOpen, text='Open', command=executer).place(x=0,y=50)
    webOpen.mainloop()