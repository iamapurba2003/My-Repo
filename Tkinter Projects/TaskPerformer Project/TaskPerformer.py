from tkinter import *
from tkinter.ttk import *
import WikiSearch 
import FileOpen
import WA
import YT
import WebSearch
import WebLink
import SysDown
import Email

window = Tk()
window.title('Task Performer')
window.geometry('300x200')
str1 = StringVar()


def commands():
    
    # For Sending a WA Message
    if str1.get() == 'Send a WA Message':
        WA.main()

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
window.update()

okButton =Button(window, text="Ok", command=commands)
okButton.place(x=10, y=60, anchor='nw')
window.update()

okButton =Button(window, text="Quit", command=window.destroy)
okButton.place(x=90, y=60, anchor='nw')
window.update()

window.mainloop()
