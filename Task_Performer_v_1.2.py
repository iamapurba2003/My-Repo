try:
    import pywhatkit as kit
    #install pywhatkit if not installed earlier
    
    import smtplib

    import os

    import webbrowser as wb

    try:
        while True:
            print('Hello, What task do you want to perform?\n1. Send a WhatsApp Message\n2. Play on YouTube\n3. Search on Web\n4. Search on Wikipedia\n5. Open files on this computer\n6. Shut Down the system\n7. Open any web link\n8. Send an Email\nOr simply press Enter to exit...')
            print()
            print("Enter the option no. from above:")
            option = int(input(""))
    
            if option == 1:
                print('Ok...')
                dial_code = str(input("Enter the country's dialling code(ignore (+)): "))
                contact = str(input("Enter receiver's number: "))
                msg = str(input('Enter the message: '))
                time1 = int(input("Enter the time(hour unit): "))
                time2 = int(input("Enter the time(min. unit): "))
                delay = int(input("Set delay(min:10): "))
                dial = ("+"+dial_code+contact)
                kit.sendwhatmsg(dial, msg, time1, time2, delay)
                #kit.sendwhatmsg() is receiver number, msg, hr, min,delay,sleep

            if option == 2:
                print('Enter the keyword:')
                keyword = str(input())
                print("Opening on YouTube")
                kit.playonyt(keyword)
                print()

            if option == 3:
                print("Ok... Enter the keyword:")
                searchword = str(input())
                print("Opening Google and searching")
                kit.search(searchword)
                print()
            
            if option == 4:
                print("Ok... Enter the keyword to search: ")
                while True:
                    
                    wikisearch = input()
                    if wikisearch == "":
                        break
                    else:    
                        print('Searching...')
                        print()
                    try:
                        kit.info(wikisearch)
                        break
                    except Exception:
                        print("Error! Try using other keywords...")
                        continue
                
            if option == 5:
                print('Enter the file path:')
                path = input("")
                try:
                    print("Opening...")
                    os.startfile(path)
                except FileNotFoundError:
                    print("Can't find the file according to the given path")
                    print()

            if option == 6:
                print("Ok... Set the countdown timer(secs):")
                countdown = int(input())
                kit.shutdown(countdown)
                print('Your system will shut down in',countdown,'seconds')
                print()
                

            if option == 7:
                print("Enter the link: ")
                link1 = input()
                print("Opening link...")
                wb.open_new_tab(link1)
                print()
            
            if option == 8:
                print("To use this service, you would need to turn on 'Less Secure app access' under security tab of your google account")
                print("CAUTION: If you have enabld two step verification then disable it...")
                while True:
                    try:
                        user_info = input("Enter your mail address: ")
                        user_pass = input("Enter your password: ")
                        mailAddress = input("Enter recipient's mail address: " )
                        text = input("Enter message to be sent: ")


                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(user_info, user_pass)
                        server.sendmail(user_info , mailAddress, text)
                        print("Voila! Your mail was sent successfully...")
                        break
                        
                    except Exception:
                        print("Your mail was not \"Sent\" due to some potential errors...")
                        break
            
            if option == 9:
                print("Do you want to cancel scheduled shutdown?\n1. Yes\n2. No")
                cancel = int(input('Enter numeric input: '))
                if cancel == 1:
                    kit.cancelShutdown()
                    print("Scheduled ShutDown cancelled...")
                    print()
                else:
                    print()              
                    continue
            else:
                print("Choose a valid option!")
                print("-"*30)

                continue






            print('Wanna perform any other task again?\n1. Yes\n2. No')
            run = int(input('Enter option number: '))
            if run == 1:
                print('Ok')
                print('-'*25)
                continue
                
            if run == 2:
                print("Have a good day!!")
                break
    except ValueError:
        print("Have a good day!!")
except ModuleNotFoundError:
    print('INSTALL REQUIRED MODULES: pywhatkit')
