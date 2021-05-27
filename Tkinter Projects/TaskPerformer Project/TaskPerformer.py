from tkinter import *
from tkinter.ttk import *
import WikiSearch 
import FileOpen
import YT
import WebSearch
import WebLink
import SysDown
import Email
import pywhatkit as kit
import tkinter.messagebox as mb

window = Tk()
window.title('Task Performer')
window.geometry('300x200')
str1 = StringVar()


def commands():
    
    # For Sending a WA Message
    if str1.get() == 'Send a WA Message':
        import WA
        # new = Tk()
        # new.geometry('300x300')
        # new.title('Send WA Message')

        # phoneNumber = StringVar()
        # hourTime = IntVar()
        # minTime = IntVar()
        # delayTime = IntVar()


        # Label(new, text="Enter recipient's no.:").place(x=0, y=0)
        # Label(new, text="Please enter the phone number \nalong with the Country's ISD Code",foreground='red').place(y=20)

        # phone = Text(new,  width=25, height=1)
        # phone.place(x = 115)

        # Label(new, text='Enter message the message for the recipient:').place(x=0,y=70)

        # message = Text(new, width=25, height=6)
        # message.place(x=0,y=90)
        

        # Label(new, text='HH:MM').place(x=0,y=200)
        # Label(new, text=':').place(x=92,y=200)

        # # def hourset(event='<Return>'):
        # #     hour= event.get()
        # #     # return int(hour)
        # #     print(hour)
        
        # # def minset(event='<Return>'):
        # #     minute = minTime.get()
        # #     return int(minute)

        # timeHour = Entry(new, width=3, textvariable=hourTime)
        # timeHour.place(x=50,y=200)
        # # timeHour.bind('<<ComboboxSelected>>',hourset)

        # timeMin = Entry(new, width=3, textvariable=minTime)
        # timeMin.place(x=100,y=200)
        # # timeMin.bind('<<ComboboxSelected>>', minset)

        # Label(new, text='Set Delay:').place(y=230)
        # Label(new, text='seconds').place(x=110,y=230)
        # delay = Combobox(new, width=4, textvariable=delayTime, values=(15,20,25,30), state='readonly')
        # delay.place(x=60, y=230)

        # def send():
        #     store = (message.get('1.0','end'))
        #     contact = phone.get('1.0','end')
        #     hour = hourTime.get()
        #     minute = minTime.get()
        #     delaytimer = delayTime.get()
        #     try:
        #         if minTime.get() <10:
        #             if mb.showinfo('Send WA Message', f"Message will be sent at {hour}:0{minute}"):
        #                 mb.showinfo('Send WA Message','Feel free to keep using your PC!')
        #                 kit.sendwhatmsg(contact, store, hour, minute, delaytimer)
        #                 mb.showinfo('Send WA Message', 'Message sent successfully!')
                    
        #         else:
        #             if mb.showinfo('Send WA Message', f"Message will be sent at {hour}:{minute}"):
        #                 mb.showinfo('Send WA Message','Feel free to keep using your PC!')
        #                 kit.sendwhatmsg(contact, store, hour, minute, delaytimer)
        #                 mb.showinfo('Send WA Message', 'Message sent successfully!')
        #     except Exception as e:
        #         mb.showerror('Error!',e)
            


        # Button(new, text='Send!', command=send).place(x=220, y= 125)
        # new.mainloop()









    # For playing content on YouTube
    if str1.get() == 'Play on YouTube':
        YT.main()
    
    # For a Web Search
    elif str1.get() == 'Search on Web':
        WebSearch.mainFunc()

    # Search on Wikipedia
    elif str1.get() == 'Search on Wikipedia':
        WikiSearch.main()

    # Open Files on this Computer
    elif str1.get() == 'Open files on this computer':
        FileOpen.main()
    
    # Shut down the System
    elif str1.get() == 'Shut Down the system':
        SysDown.mainExecution()
    
    # Open a web link
    elif str1.get() == 'Open any web link':
        WebLink.main()
    
    # Send an Email
    elif str1.get() == 'Send an Email':
        Email.main()

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

okButton =Button(window, text="Ok", command=commands)
okButton.place(x=10, y=60, anchor='nw')

okButton =Button(window, text="Quit", command=window.destroy)
okButton.place(x=90, y=60, anchor='nw')

window.mainloop()
