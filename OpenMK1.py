import os
import webbrowser

while True:
    print("What will you open?")
    print("1. File using the file address\n2. Weblink or\n3. Exit this Program")
    try:
        inpt = int(input("Enter option of your choice: "))
    
        if inpt == "":
            print("Have a good day ahead!!")
            break
        if inpt == 1:
            try:
                addr = input("Enter the file address: ")
                if addr == "":
                    print("Have a good day ahead!!")
                    break
                else:
                    os.startfile(addr)
                    print('-'*50)
            except FileNotFoundError:
                print("Can't find file according to path specified.")
                
        if inpt == 2:
            website = input("Enter the web address: ")
            if website == "":
                print("Have a good day ahead!!")
                break
            else:
                webbrowser.open_new_tab(website)
                print('-'*50)
        if inpt == 3:
            print("Have a good day!!")
            break
    except ValueError:
        print("Please enter numeric input only.")
        print()
        print('-'*50)
            
            



