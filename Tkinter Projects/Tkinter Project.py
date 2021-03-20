

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

# root.geometry("600x300")
root.maxsize(800, 400)
root.minsize(200, 200)

root.title("SignUp Page")


userInput= StringVar()
password = StringVar()

sql = f"select username from logins"
myCursor.execute(sql)
fetch=myCursor.fetchall()
store = []
for i in range(0,len(fetch)):
    store.append(fetch[i][0])

sql1 = "select password from logins"
myCursor.execute(sql1)
fetch1 = myCursor.fetchall()
pwdstore = []
for i in range(len(fetch1)):
    pwdstore.append(fetch1[i][0])

def mainFuntion():
    var1 = False
    var2 = False
    namevar = False
    namevar2 =False
    executer = False
    
    listEmpty=[]
    list1= ['red', 'orange', 'violet', 'blue', 'green', 'black', 'white']
    user1 = userInput.get()
    pwd = password.get()

    for i in range(len(pwd)):
        if pwd[i].isupper() == True:
            var1 = True
        
        if pwd[i] not in """-_!@#$%^&'"*()|+=?\/><:;[]}{""":
            var2 = False
        
        if pwd[i] in """-_!@#$%^&*()|+=?'"\/><:;[]}{""":
            var2 = True

    for i in range(len(user1)):
            if user1[i].casefold() in "abcdefghijklmnopqrstuvwxyz":
                namevar = True
            
            if user1[i].isupper() == True:
                namevar = True
                
            if user1[i] in "0123456789":
                namevar2 = True
    
    if user1 == '' and pwd == '':
        executer = True
        newLabel1= Label(root, text='Please fill above fields', foreground=list1[random.randint(0,6)])
        newLabel1.grid(row=5,column=1)
        root.update()
    
    
    
    if executer == False:
        if user1 in store:
            newLabel1= Label(root, text='Username is already taken', foreground=list1[0])
            newLabel1.grid(row=0, column=2)
            root.update()
                
        if namevar != True:
            newlabel1 = Label(root, text="Alphabets missing in username!", foreground=list1[0])
            newlabel1.grid(row=0, column=2)
            root.update()

        if namevar2 != True:
            newlabel5 = Label(root, text="Numbers are missing in username!", foreground= list1[0])
            newlabel5.grid(row=0, column=2)
            root.update()

        if user1 not in store:
            newlabel7 = Label(root, text="Username is available, ✓", foreground= list1[4])
            newlabel7.grid(row=0, column=2)
            root.update()
        
        if var1 == var2 == True and pwd in pwdstore:
            newLabel1= Label(root, text='Try choosing a different password', foreground=list1[0])
            newLabel1.grid(row=3, column=1)
            root.update()

    
        if pwd == '':
            newlabel3 = Label(root, text='Password field cannot be left empty!', foreground=list1[0])
            newlabel3.grid(row=3,column=1)
            root.update()
        
        if var1 == var2 == True and pwd not in pwdstore:
            newlabel3 = Label(root, text='Password criterion are successful!', foreground=list1[4])
            newlabel3.grid(row=3,column=1)
            root.update()

        if var1 == var2 == False:
            newlabel3 = Label(root, text='Uppercase and special characters absent', foreground=list1[0])
            newlabel3.grid(row=3,column=1)
            root.update()

        if var1 == False and var2 == True:
            wrongLabel = Label(root, text="Password fails in having an Uppercase letter",foreground=list1[0])
            wrongLabel.grid(row=1,column=2)
            root.update()
            
        if var1 == True and var2 == False:
            wrongLabel1 = Label(root, text="Password fails in having a special Character", foreground=list1[0])
            wrongLabel1.grid(row=1,column=2)
            root.update()
        
        
        if user1 == '':
            newlabel4=Label(root, text='Enter username!', foreground=list1[0])
            newlabel4.grid(row=0, column=2)
            root.update()

        if len(pwd)<8:
            newlabel3 = Label(root, text='Password < 8 characters!', foreground=list1[0])
            newlabel3.grid(row=1,column=2)
            root.update()

        if (user1 not in store) and (' ' not in user1) and (len(pwd)>=8) and (var1 == True and var2 == True and namevar == True and namevar2 ==True) and (pwd not in pwdstore):
        # else:  
            listEmpty.extend([user1,pwd])
            sql = "insert into logins (username, password) values (%s, %s)"
            val1 = tuple([user1, pwd])
            myCursor.execute(sql, val1)
            db.commit()

            newLabel = Label(root, text="Sign up Successful!")
            newLabel.grid(row=5, column=1)
            root.update()
            
            def NameSearch():
                UserLabel = Label(root, text=f'username: \'{listEmpty[0]}\'  password: \'{listEmpty[1]}\'')
                UserLabel.grid(column=1)
                return True
            
            newButton2= Button(root, text="Show", command=NameSearch)
            newButton2.grid(row = 6, column=1)
            root.update()
            
            newButton1 = Button(root,text="Quit",command=root.destroy)
            newButton1.grid(row =7, column=1)
            
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

newlabel2= Label(root, text='Password must have atleast 8 characters and should contain an UpperCase and special chars\nUsername should be of Alphanumeric', foreground='red')
newlabel2.grid(row=4, column=1)


button1 = Button(root, text="Sign Up", command=mainFuntion)
button1.grid(row=6, column=1)

button2 = Button(root, text="Cancel", command=root.destroy)
button2.grid(row=7,column=1)


root.mainloop()








































