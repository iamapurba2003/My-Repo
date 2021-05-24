try:
    from tkinter import *
    from tkinter.ttk import *
    import pywhatkit as kit
    from tkinter import *
    from tkinter.ttk import *
    import tkinter.messagebox as mb
    import tkinter.filedialog as fd
    import os
    window = Tk()
    window.update()
    str1 = StringVar()

    storer = ''

    def commands():
        
        # For Sending a WA Message
        if str1.get() == 'Send a WA Message':
            new = Tk()
            new.geometry('300x300')
            new.title('Send a WhatsApp Message')

            Label(new, text="Enter receiver's number: ").place(x=0, y=0)
            number = Text(new, height=1, width=20, font=('Segoe UI', 9))
            number.place(x = 135, y = 0)

            Label(new, text='Enter message: ').place(x=0, y=30)
            msg = Text(new, height=4, width=20, font=('Segoe UI', 9))
            msg.place(x = 85, y = 30)

            hrvar = IntVar()
            minvar = IntVar()
            Label(new, text= "HH : MM").place(x=0, y = 105)
            Label(new, text= ":",font=('Segoe UI',10)).place(x=105, y = 105)
            hr, min = Combobox(new, width=3,textvariable=hrvar, values=([i for i in range(0,24)])), Combobox(new, width=3,textvariable=minvar, values=([i for i in range(0,60)]))
            hr['state'],min['state']='readonly','readonly'
            hr.place(x = 65, y = 105)
            min.place(x = 115, y = 105)

            var=IntVar()
            Label(new, text='Set Delay').place(x=0,y=135)
            Label(new, text='seconds').place(x=105,y=135)
            delay=Combobox(new,textvariable=var, width=3)
            delay['values']=(
                15,
                20,
                25,
                30
            )
            delay['state'] = 'readonly'
            delay.current(0)
            delay.place(x=65,y=135)

            def sender():
                try:
                    kit.sendwhatmsg(number.get('1.0','end'),message=msg.get('1.0','end'), time_hour=hrvar.get(),time_min=minvar.get(),wait_time=var.get())
                    if minvar.get() < 10:
                        mb.showinfo(title='Success!',message=f'Message sent at {hrvar.get()}:0{minvar.get()}Hrs')
                    else:
                        mb.showinfo(title='Success!',message=f'Message sent at {hrvar.get()}:{minvar.get()}Hrs')
                except Exception as e:
                    
                    mb.showerror(title='Not Sent', message=e)
                    return 0

            sendButton = Button(new, text='Send!', command=sender)
            sendButton.place(x=70,y=170)
            new.mainloop()

        # For playing content on YouTube
        if str1.get() == 'Play on YouTube':
            new =Tk()
            key =StringVar()
            Label(new, text='Enter keyword: ').place(y=1, anchor='nw')

            keyword = Text(new, width=40, height=1, font=('Segoe UI', 11))
            keyword.place(x=80, anchor='nw')
            keyword.focus()
            
            def player():
                main = keyword.get('1.0','end')
                kit.playonyt(main)
                Label(new, text='Opening on YouTube').place(x = 80, y=30)
            Button(new, text="Go!",command=player).place(y=30)
            new.mainloop()    
        
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

except Exception:
    import tkinter.messagebox as mb
    from tkinter import *
    from tkinter.ttk import *
    msgTk= Tk()
    msgTk.geometry('300x100')
    msgTk.title('Task Performer')
    mb.showerror("Connection Error!", "This Program requires an active interet connection!")
    msgTk.title("Can't Load! - Error!")
    Button(msgTk, text='Quit', command= msgTk.destroy).place(x=110,y=40)
    msgTk.mainloop()