

#!===========================================================================================!
#!Modules!
import random
from tkinter import *
from tkinter.ttk import *
import mysql.connector as mc

db = mc.connect(host='localhost', user='root', passwd='root', database= 'testimonials')
myCursor = db.cursor()

# myCursor.execute('create table logins (username varchar(255), password varchar(255))')
# myCursor.execute('drop table if exists logins')

root = Tk()

root.geometry("500x400")
root.title("SignUp Page")

userInput= StringVar()
password = StringVar()

sql = f"SELECT username FROM logins"
myCursor.execute(sql)
fetch=myCursor.fetchall()
store = []
for i in range(0,len(fetch)):
    store.append(fetch[i][0])
    



def mainFuntion():
    listEmpty=[]
    list1= ['red', 'orange', 'violet', 'blue', 'green', 'black']
    user1 = userInput.get()
    pwd = password.get()
          
    
    if user1 == '' and pwd == '':
        
        newLabel1= Label(root, text='Please fill above fields', foreground=list1[random.randint(0,5)])
        newLabel1.grid(column=1)
        root.update()
    
     
    if user1 in store:
        newLabel1= Label(root, text='X', foreground=list1[0])
        newLabel1.grid(row=0, column=2)
        root.update()

    if user1 not in store:
        newLabel1= Label(root, text='O', foreground=list1[4])
        newLabel1.grid(row=0, column=2)
        root.update()

        
    
    if ' ' in user1:
        
        newlabel4=Label(root, text='X', foreground=list1[random.randint(0,5)])
        newlabel4.grid(row=0, column=2)
        root.update()

    if len(pwd)<8:
        
        newlabel3 = Label(root, text='Password < 8 characters!', foreground=list1[random.randint(0,5)])
        newlabel3.grid(row=1,column=2)
        root.update()

    if len(pwd)>=8:
        if len(pwd)>8:
            newlabel3 = Label(root, text='Password > 8 characters!', foreground=list1[4])
            newlabel3.grid(row=1,column=2)
            root.update()
        
        if len(pwd)==8:
            newlabel3 = Label(root, text='Password = 8 characters!', foreground=list1[4])
            newlabel3.grid(row=1,column=2)
            root.update()


    if (user1 not in store) and (' ' not in user1) and (len(pwd)>=8):
        listEmpty.extend([user1,pwd])

        sql = "insert into logins (username, password) values (%s, %s)"
        val1 = tuple([user1, pwd])
        myCursor.execute(sql, val1)
        db.commit()

        newLabel = Label(root, text="Sign up Successful!")
        newLabel.grid(row=4, column=1)
        root.update()
        
        def NameSearch():
            sql = "select username from logins"
            myCursor.execute(sql)
            fetcher1 = myCursor.fetchall()
            
            sql = "select password from logins"
            myCursor.execute(sql)
            fetcher2 = myCursor.fetchall()

            db.commit()
            UserLabel = Label(root, text=f'username: \'{listEmpty[0]}\'  password: \'{listEmpty[1]}\'')
            UserLabel.grid(column=1)
            return True
        
        newButton2= Button(root, text="Show", command=NameSearch)
        newButton2.grid(row=5, column=1)
        # print(listEmpty)
        newButton1 = Button(root,text="Quit",command=root.destroy)
        newButton1.grid(row=6, column=1)
        
        return True
    

nameLabel = Label(root, text='User Name: ')
nameLabel.grid(row=0, column=0)

nameEntry = Entry(root, width=20, textvariable=userInput)
nameEntry.grid(row=0, column=1)
nameEntry.focus()

passLabel = Label(root,text="Password: ")
passLabel.grid(row=1, column=0)

passEntry =  Entry(root, width=20,textvariable=password)
passEntry.grid(row=1, column=1)
passEntry.focus()

newlabel2= Label(root, text='Password should have atleast 8 characters', foreground='red')
newlabel2.grid(row=2, column=1)


button1 = Button(root, text="Sign Up", command=mainFuntion)
button1.grid(row=3, column=1)

button2 = Button(root, text="Cancel", command=root.destroy)
button2.grid(row=4,column=1)


root.mainloop()














































