from tkinter import *
from tkinter.ttk import *
import pywhatkit as kit
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb

def mainExecution():
    shut = Tk()
    shut.title('Sign Out')

    numTime = IntVar()
    timeUnit = StringVar()
    num = numTime.get()

    def runner():
        if timeUnit.get() == 'seconds' or timeUnit.get() == 'second':
            kit.shutdown(numTime.get())
            mb.showwarning('Sign Out!', f"You will be Signed Out in {numTime.get()} {timeUnit.get()}!")
            if mb.askyesnocancel('Cancel Sign Out?', 'Do you want to cancel Shut Down?') == True:
                kit.cancelShutdown()
        
        elif timeUnit.get() == 'minutes' or timeUnit.get() == 'minute':
            kit.shutdown(numTime.get()*60)
            mb.showwarning('Sign Out!', f"You will be Signed Out in {numTime.get()} {timeUnit.get()}!")
            if mb.askyesnocancel('Cancel Sign Out?', 'Do you want to cancel Shut Down?') == True:
                kit.cancelShutdown()
        
        else:
            kit.shutdown(numTime.get()*3600)
            mb.showwarning('Sign Out!', f"You will be Signed Out in {numTime.get()} {timeUnit.get()}!")
            if mb.askyesnocancel('Cancel Sign Out?', 'Do you want to cancel Shut Down?') == True:
                kit.cancelShutdown()
        

    def refresher(func):
        Label(shut, text=f'You will Sign Out in {numTime.get()} {timeUnit.get()}!                  ').place(x=20,y=100)


    def preview(func):
        global unit
        if numTime.get() >1:
            unit = Combobox(shut, width=8, values=('seconds', 'minutes','hours'), textvariable=timeUnit)
            unit.place(x=60,y=30)
            unit.current(0)
            unit.bind('<<ComboboxSelected>>', refresher)
            Button(shut, text='Ok', command=runner).place(x=70,y=70)
        else:
            unit = Combobox(shut, width=8, values=('second', 'minute','hour'), textvariable=timeUnit)
            unit.place(x=60,y=30)
            unit.current(0)
            unit.bind('<<ComboboxSelected>>', refresher)
            Button(shut, text='Ok', command=runner).place(x=70,y=70)


    Label(shut, text='Set Delay:').place(x=10,y=10)
    timer = Combobox(shut, width=4, values=(1,2,3,5,10,15,30,45),textvariable=numTime)
    timer.place(x=10,y=30)
    timer.bind('<<ComboboxSelected>>',preview)



    shut.mainloop()