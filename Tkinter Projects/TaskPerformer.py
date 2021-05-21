import tkinter as tk
import tkinter.ttk as ttk
import pywhatkit as kit
window = tk.Tk()
str1 = tk.StringVar()
def commands():
    commandList = [
    'Send a WhatsApp Message',
    'Play on YouTube',
    'Search on Web',
    'Search on Wikipedia',
    'Open files on this computer',
    'Shut Down the system', 
    'Open any web link',
    'Send an Email'
    ]

    if str1.get() == commandList[0]:
        new = tk.Tk()
        lbl = ttk.Label(new, text="Enter the receiver's number: +")
        lbl.place(x=1,y=1,anchor='nw')
        new.mainloop()
    
    elif str1.get() == commandList[1]:
        print("Hi1")
    
    elif str1.get() == commandList[2]:
        print('Hi2')
    
    elif str1.get() == commandList[3]:
        print('hi3')

    elif str1.get() == commandList[4]:
        print('hi4')
        
    elif str1.get() == commandList[5]:
        print('hi5')

    elif str1.get() == commandList[6]:
        print('hi6')

    elif str1.get() == commandList[7]:
        print('hi7')

    elif str1.get() == '<Select>':
        print('Select something Bitch!')

combo = ttk.Combobox(window, textvariable=str1, width=25)
combo['values'] = (
    '<Select>',
    'Send a WhatsApp Message',
    'Play on YouTube',
    'Search on Web',
    'Search on Wikipedia',
    'Open files on this computer',
    'Shut Down the system', 
    'Open any web link',
    'Send an Email'
)
combo.current(0)
combo.place(x=10, y=10, anchor='nw')

okButton = ttk.Button(window, text="Ok", command=commands)
okButton.place(x=10, y=60, anchor='nw')
window.mainloop()
print(str1.get())