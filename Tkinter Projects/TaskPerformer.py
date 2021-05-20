import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry("300x300")

option = tk.IntVar()
def commands():
    if option.get() == 1:
        ttk.Label(tk.Tk(), text="Hello").grid()
        tk.mainloop()
    
    elif option.get() == 2:
        ttk.Label(tk.Tk(), text="Hello 2").grid()
        tk.mainloop()
    
    elif option.get() == 3:
        ttk.Label(tk.Tk(), text="Hello 3").grid()
        tk.mainloop()
    
    elif option.get() == 4:
        ttk.Label(tk.Tk(), text="Hello 4").grid()
        tk.mainloop()
    
    elif option.get() == 5:
        ttk.Label(tk.Tk(), text="Hello 5").grid()
        tk.mainloop()
    
    elif option.get() == 6:
        ttk.Label(tk.Tk(), text="Hello 6").grid()
        tk.mainloop()


option1 = ttk.Radiobutton(window, text='Option 1', value=1, variable=option, command=commands)
option1.grid(row=1, column=1)

option2 = ttk.Radiobutton(window, text='Option 2', value=2, variable=option, command=commands)
option2.grid(row=2, column=1)

option3 = ttk.Radiobutton(window, text='Option 3', value=3, variable=option, command=commands)
option3.grid(row=3, column=1)

option4 = ttk.Radiobutton(window, text='Option 4', value=4, variable=option, command=commands)
option4.grid(row=4, column=1)

option5 = ttk.Radiobutton(window, text='Option 5', value=5, variable=option, command=commands)
option5.grid(row=5, column=1)

option6 = ttk.Radiobutton(window, text='Option 6', value=6, variable=option, command=commands)
option6.grid(row=6, column=1)


window.mainloop()
print(option.get())