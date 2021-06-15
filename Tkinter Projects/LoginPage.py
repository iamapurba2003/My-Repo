#Importing modules required for this project
from tkinter import *
from tkinter.ttk import *
import mysql.connector as mc
import SignUp as sn

#Initialising the connection with the database
dbLogin = mc.connect(host = 'localhost', user="root", passwd="root", database="testimonials")
myCursor = dbLogin.cursor()

#Deploying SQL commands for python
sql = "select * from logins"
myCursor.execute(sql)
fetcher =  myCursor.fetchall()
credenDict ={}
usernames = []
for i in range(len(fetcher)):
    credenDict.update({fetcher[i][0]:fetcher[i][1]})
    usernames.append(fetcher[i][0])

#Setting up root and configuring it for initialising the Tkinter Window.
root = Tk()
root.title("Login Page")
root.geometry("300x150")

#Tkinter runtime variables
username = StringVar()
password = StringVar()

#defining a function for username and password validations
def credentials():
    user = username.get()
    passwd = password.get()
    
    if user in usernames:
        userVal = credenDict.get(user)
        newLabel2 = Label(root, text="Username not found", foreground='white')
        newLabel2.grid(row=0, column=2)
        root.update()
        if passwd != userVal:
            newLabel3 = Label(root, text="Password incorrect", foreground='red')
            newLabel3.grid(row=1, column=2)

    if user not in usernames:
        newLabel2 = Label(root, text="Username not found", foreground='red')
        newLabel2.grid(row=0, column=2)
        sn.main()

    if user in usernames and passwd == userVal:
        newLabel3 = Label(root, foreground='white', text='Password incorrect')
        newLabel3.grid(row=1, column=2)
        root.update()
        newLabel2 = Label(root, text="Username not found", foreground='white')
        newLabel2.grid(row=0, column=2)
        root.update()
        newLabel = Label(root, text=f"Welcome, {user}!", foreground='green')
        newLabel.grid(row=2, column=1)


#Username Entry part
usernameLabel = Label(root, text="Username: ", foreground='black')
usernameLabel.grid(row=0, column=0)

userboxLabel = Entry(root, width=15, textvariable=username)
userboxLabel.grid(row=0, column=1)
userboxLabel.focus()

#Password Entry part
passwordLabel = Label(root, text="Password: ", foreground="black")
passwordLabel.grid(row=1, column=0)

passwordboxLabel = Entry(root, textvariable=password, width=15)
passwordboxLabel.grid(row=1, column=1)

#setting up buttons for credentials checking & execution and for exiting the program
loginButton = Button(root, text="Login/SignUp", command=credentials)
loginButton.grid(row=3, column=1)

quitButton = Button(root, text='Quit', command=root.destroy)
quitButton.grid(row=4, column=1)

#Executing the Tkinter window
root.mainloop()
