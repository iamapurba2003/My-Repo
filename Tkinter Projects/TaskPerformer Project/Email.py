from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox as mb
import smtplib as mailer
def main():
    mail = Tk()
    mail.title('Send an Email')
    mail.geometry('360x300')

    optionNum=IntVar()
    usermail = StringVar()
    passwordManager = StringVar()
    receivermail = StringVar()

    Message(mail, text="🛑Make sure you've turned on less secure app access in your mail a/c!", foreground='red').place(x=210, y=0)
    Label(mail, text='Enter your mail:').place(x=0,y=0)
    sender = Entry(mail, width=30, textvariable=usermail)
    sender.place(x=0,y=20)

    Label(mail, text='Enter your password:').place(x=0,y=47)
    password = Entry(mail, width=25, show='•', textvariable=passwordManager)
    password.place(x=0,y=67)

    def showhide(event='<Return>'):
        if optionNum.get() == 1:
            password['show'] = ''
        
        else:
            password['show'] = '•'


    Checkbutton(mail, text='Show',onvalue=1, offvalue=0, variable=optionNum, command=showhide).place(x=160,y=70)

    Label(mail, text="Enter recipient's mail:").place(x=0, y=95)
    receiver = Entry(mail, width=25, textvariable=receivermail)
    receiver.place(x=0, y=115)

    def send(event='<Return>'):
        try:
            server = mailer.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(usermail.get(), passwordManager.get())
            server.sendmail(usermail.get(), receivermail.get(), message.get('1.0', 'end'))
            mb.showinfo('Success!', 'Mail Sent Successfully!')
        except Exception as e:
            mb.showerror("Couldn't Send! - Error!", 'Not SENT due to errors!')


    Label(mail, text='Enter message for recipient:').place(x=0,y=139)
    message=Text(mail, width=25, height=8)
    message.place(x=0,y=159)


    Button(mail, text='Send!', command=send).place(x=210,y=159)
    mail.mainloop()