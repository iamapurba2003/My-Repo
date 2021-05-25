from tkinter import *
from tkinter.ttk import *
import pywhatkit as kit
import tkinter.messagebox as mb

def main():
    new = Tk()
    new.geometry('300x300')
    new.title('Send WA Message')

    phoneNumber = StringVar()
    hourTime = IntVar()
    minTime = IntVar()
    delayTime = IntVar()


    Label(new, text="Enter recipient's no.:").place(x=0, y=0)
    Label(new, text="Please enter the phone number \nalong with the Country's ISD Code",foreground='red').place(y=20)

    phone = Entry(new,  width=25, textvariable=phoneNumber)
    phone.place(x = 115)
    phone.focus()

    Label(new, text='Enter message the message for the recipient:').place(x=0,y=70)

    message = Text(new, width=25, height=6)
    message.place(x=0,y=90)

    Label(new, text='HH:MM').place(x=0,y=200)
    Label(new, text=':').place(x=92,y=200)

    timeHour = Combobox(new, width=3, values=([i for i in range(0,24)]), textvariable=hourTime)
    timeHour.place(x=50,y=200)

    timeMin = Combobox(new, width=3, textvariable=minTime, values=([i for i in range(0,60)]))
    timeMin.place(x=100,y=200)

    Label(new, text='Set Delay:').place(y=230)
    Label(new, text='seconds').place(x=110,y=230)
    delay = Combobox(new, width=4, textvariable=delayTime, values=([i for i in range(15, 31) if i%5==0]), state='readonly')
    delay.place(x=60, y=230)

    def send():
        try:
            if minTime.get() <10:
                if mb.showinfo('Send WA Message', f"Message will be sent at {hourTime.get()}:0{minTime.get()}"):
                    mb.showinfo('Send WA Message','Feel free to keep using your PC!')
                    kit.sendwhatmsg(phoneNumber.get(), message.get('1.0', 'end'), hourTime.get(), minTime.get(), delayTime.get())
                    mb.showinfo('Send WA Message', 'Message sent successfully!')
                
            else:
                if mb.showinfo('Send WA Message', f"Message will be sent at {hourTime.get()}:{minTime.get()}"):
                    mb.showinfo('Send WA Message','Feel free to keep using your PC!')
                    kit.sendwhatmsg(phoneNumber.get(), message.get('1.0', 'end'), hourTime.get(), minTime.get(), delayTime.get())
                    mb.showinfo('Send WA Message', 'Message sent successfully!')
        
        except Exception as e:
            mb.showerror('Error!', e)


    Button(new, text='Send!', command=send).place(x=220, y= 125)
    new.mainloop()
