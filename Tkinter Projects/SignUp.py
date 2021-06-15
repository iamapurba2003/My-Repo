
#!===========================================================================================!
#!Modules!
import random
from tkinter import *
from tkinter.ttk import *
import mysql.connector as mc
def main():
    #Creating conection with the databse
    db = mc.connect(host='localhost', user='root', passwd='root', database= 'testimonials')
    myCursor = db.cursor()


    #initiating the  main window based on root
    root = Tk()


    #setting the max and min width and height of window
    root.maxsize(800, 400)
    root.minsize(200, 200)


    #adding title
    root.title("SignUp Page")


    #assigning the input to be taken during tkinter runtime into the specified variables
    userInput= StringVar()
    password = StringVar()


    #checking all the usernames and storing them in an empty list
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

        
    #defining the main function with some conditions and tkinter widgets
    def mainFunction():
        var1 = False
        var2 = False
        namevar = False
        namevar2 =False
        executer = False
        
        listEmpty=[]
        list1= ['red', 'orange', 'violet', 'blue', 'green', 'black', 'white']
        user1 = userInput.get()
        pwd = password.get()

        
        #running check process for the password authentication and so for username
        for i in range(len(pwd)):
            if pwd[i].isupper() == True:
                var1 = True
            
            if pwd[i] in """-_!@#$%^&*()|+=?'"\/><:;[]}{""":
                var2 = True

        for i in range(len(user1)):
                if user1[i].casefold() in "abcdefghijklmnopqrstuvwxyz":
                    namevar = True
                
                if user1[i].isupper() == True:
                    namevar = True
                    
                if user1[i] in "0123456789":
                    namevar2 = True

                    
        #setting conditions for proper execution
        if user1 == '' and pwd == '':
            executer = True
            newLabel1= Label(root, text='Please fill above fields', foreground=list1[random.randint(0,6)])
            newLabel1.grid(row=5,column=1)
            root.update()
        
        if executer == False:
            if user1 in store:
                newLabel1= Label(root, text='Username already taken', foreground=list1[0])
                newLabel1.grid(row=0, column=2)
                root.update()
                    
            if namevar != True:
                newlabel1 = Label(root, text="Alphabets missed", foreground=list1[0])
                newlabel1.grid(row=0, column=2)
                root.update()

            if namevar2 != True:
                newlabel5 = Label(root, text="Numbers missed", foreground= list1[0])
                newlabel5.grid(row=0, column=2)
                root.update()

            if user1 not in store and namevar == namevar2 == True:
                newlabel7 = Label(root, text="Username is available, ✓", foreground= list1[4])
                newlabel7.grid(row=0, column=2)
                root.update()
            
            if var1 == var2 == True and pwd in pwdstore:
                newLabel1= Label(root, text='Try choosing a different password', foreground=list1[0])
                newLabel1.grid(row=3, column=1)
                root.update()

            if pwd == '':
                newlabel3 = Label(root, text='Password cannot be left empty!', foreground=list1[0])
                newlabel3.grid(row=3,column=1)
                root.update()
            
            if var1 == var2 == True and pwd not in pwdstore:
                newlabel3 = Label(root, text='Password criterion are successful!', foreground=list1[4])
                newlabel3.grid(row=3,column=1)
                root.update()

            if var1 == var2 == False:
                newlabel3 = Label(root, text='Fulfill password criteria', foreground=list1[0])
                newlabel3.grid(row=3,column=1)
                root.update()

            if var1 == False and var2 == True:
                wrongLabel = Label(root, text="Uppercase letter missed",foreground=list1[0])
                wrongLabel.grid(row=1,column=2)
                root.update()
                
            if var1 == True and var2 == False:
                wrongLabel1 = Label(root, text="Special Character missed", foreground=list1[0])
                wrongLabel1.grid(row=1,column=2)
                root.update()
            
                
            if var1 == var2 == True:
                wrongLabel1 = Label(root, text="All the criterions are OK!", foreground=list1[4])
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
                listEmpty.extend([user1,pwd])
                sql = "insert into logins (username, password) values (%s, %s)"
                val1 = tuple([user1, pwd])
                myCursor.execute(sql, val1)
                db.commit()

                newLabel = Label(root, text="Sign up Successful!")
                newLabel.grid(row=5, column=1)
                root.update()
                #defining a new function for displaying the credentials at last
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
        
        
        
    #widgets to be displayed in the main window based upon root
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


    button1 = Button(root, text="Sign Up", command=mainFunction)
    button1.grid(row=6, column=1)

    button2 = Button(root, text="Cancel", command=root.destroy)
    button2.grid(row=7,column=1)


    #finally running all the codes using root.mainloop() method
    root.mainloop()

if __name__ =='__main__':
    main()