from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Cryptograph")
window.iconbitmap("D:/encryption.ico")
mainFrame = Frame(window)
mainFrame.grid(row=0, column=1)

modeMenu = StringVar()
messageMod = StringVar()


def cryptoMachine(message: str=..., mode: str=...):
    keys = """aN@E%S$bc^de!fA*g&O(h,KiJ"';C]:M.-D|~L_₹jk[Zl/Im5n6Wo1Rp9}{Xq7YrP2BHs8tG0u>?<vwTxVyUF3z+Q#*)=` """
    values = """!@#$%₹^&+-/*()}{][~`"':;.,?_|=<>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ """
    encryptionDict = dict(zip(keys, values))
    decryptionDict = dict(zip(values, keys))

    if mode == "Encrypt":
        modMessage = "".join([encryptionDict[letter] for letter in message])
        return modMessage
    
    if mode == "Decrypt":
        modMessage = "".join([decryptionDict[letter] for letter in message])
        return modMessage
        
    if mode == None:
        return None


messageSection = Label(mainFrame, text = "Enter your message: ")
messageSection.grid()

messageBox = Entry(mainFrame, width=40,textvariable=messageMod)
messageBox.grid()
messageBox.focus()

modeMenu1 = Combobox(window, textvariable=modeMenu)
modeMenu1.grid(row=1, column=1)
modeMenu1["values"] = ("Encrypt", "Decrypt")
modeMenu1["state"] = "readonly"

def main():
    CryptoMessage = cryptoMachine(messageMod.get(), modeMenu.get())
    if modeMenu.get() == "Decrypt":
        newLabel = Label(window,text="The Decrypted Message: ")
        newLabel.grid(row=7,column=1)
        window.update()

        newText = Text(window, width=20, height=4)
        newText.grid(row=8,column=1)
        window.update()
        newText.insert("1.0", f"{CryptoMessage}")

    if modeMenu.get() == "Encrypt":
        newLabel = Label(window, text="The Encrypted Message: ")
        newLabel.grid(row=7,column=1)
        window.update()

        newText = Text(window, width = 20, height = 4)
        newText.grid(row=8,column=1)
        window.update()
        newText.insert("1.0",f"{CryptoMessage}")


mainButton = Button(window, text="Ok", command=main)
mainButton.grid(row=2,column=1)
window.mainloop()
