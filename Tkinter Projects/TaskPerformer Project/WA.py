from tkinter import *
from tkinter.ttk import *
import pywhatkit as kit
import tkinter.messagebox as mb

# def main():

def receive(event='<Return>'):
    Label(new, text='Enter message the message for the recipient:').place(x=0,y=70)
    global message
    message = Text(new, width=25, height=6)
    message.place(x=0,y=90)
    message.bind('<Return>',timeSet)


def send():
    store = (message.get('1.0','end'))
    contact = phone.get('1.0','end')
    hour = hourTime.get()
    minute = minTime.get()
    delaytimer = delayTime.get()
    try:
        if minTime.get() <10:
            if mb.showinfo('Send WA Message', f"Message will be sent at {hour}:0{minute}"):
                mb.showinfo('Send WA Message','Feel free to keep using your PC!')
                kit.sendwhatmsg(contact, store, hour, minute, delaytimer)
                mb.showinfo('Send WA Message', 'Message sent successfully!')
            
        else:
            if mb.showinfo('Send WA Message', f"Message will be sent at {hour}:{minute}"):
                mb.showinfo('Send WA Message','Feel free to keep using your PC!')
                kit.sendwhatmsg(contact, store, hour, minute, delaytimer)
                mb.showinfo('Send WA Message', 'Message sent successfully!')
    except Exception as e:
        mb.showerror('Error!',e)


def senderButton():
    Button(new, text='Send!', command=send).place(x=220, y= 125)



def timeSet(event="<Return>"):
    Label(new, text='HH:MM').place(x=0,y=200)
    Label(new, text=':').place(x=72,y=200)


    timeHour = Entry(new, width=3, textvariable=hourTime)
    timeHour.place(x=50,y=200)
    # timeHour.bind('<<ComboboxSelected>>',hourset)

    timeMin = Entry(new, width=3, textvariable=minTime)
    timeMin.place(x=80,y=200)
    # timeMin.bind('<<ComboboxSelected>>', minset)

    Label(new, text='Set Delay:').place(y=230)
    Label(new, text='seconds').place(x=110,y=230)
    delay = Entry(new, width=4, textvariable=delayTime)
    delay.place(x=60, y=230)

    Button(new, text='Ok',command=senderButton).place(x=60,y=250)

    # Prototye for the method calling from another Script, does not contribute when running this script
def main():    
    new = Tk()
    new.geometry('300x300')
    new.title('Send WA Message')
    phoneNumber = StringVar()
    hourTime = IntVar()
    minTime = IntVar()
    delayTime = IntVar()
    message = 0
    Label(new, text="Enter recipient's no.:").place(x=0, y=0)
    Label(new, text="Please enter the phone number \nalong with the Country's ISD Code",foreground='red').place(y=20)

    phone = Text(new,  width=25, height=1)
    phone.place(x = 115)
    phone.bind('<Return>',receive)
    new.mainloop()

    # Solely, contributes while running this Script, does not does anything when a module is called
if __name__ == "__main__":
    new = Tk()
    new.geometry('300x300')
    new.title('Send WA Message')
    phoneNumber = StringVar()
    hourTime = IntVar()
    minTime = IntVar()
    delayTime = IntVar()
    message = 0
    Label(new, text="Enter recipient's no.:").place(x=0, y=0)
    Label(new, text="Please enter the phone number \nalong with the Country's ISD Code",foreground='red').place(y=20)

    phone = Text(new,  width=25, height=1)
    phone.place(x = 115)
    phone.bind('<Return>',receive)
    new.mainloop()
# main()
