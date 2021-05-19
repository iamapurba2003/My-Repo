import tkinter as tk
import tkinter.ttk as ttk

mainWindow = tk.Tk()
mainWindow.geometry("300x300")
grid.rowconfigure(mainWindow,0,weight=1)
grid.columnconfigureconfigure(mainWindow,0,weight=1)

ttk.Label(mainWindow, background="red").grid(row=0, column=2, columnspan=9)
ttk.Label(mainWindow, background="blue").grid(row=2, column=2, columnspan=8)
ttk.Label(mainWindow, background="green").grid(row=4, column=2, columnspan=10)

mainWindow.mainloop()
