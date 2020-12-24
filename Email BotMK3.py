import smtplib
while True:
    try:
        print("To use this feature, pls turn on \"Less Secure Apps access\" in your Google account manager settings")
        user_mail = input("Enter your mail address: ")
        user_pwd = input("Enter your mail password: ")
        
        mailAddress = input("Enter recipient's mail address: " )
        text = input("Enter message to be sent: ")


        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user_mail, user_pwd)
        server.sendmail(user_mail, mailAddress, text)
        print("Voila! Your mail was sent successfully...")
        print()
        print('Would you like to send another mail?')
        print("Y\nN")
        inpt = input("Enter your choice: ")
        if "Y" in inpt:
            continue
        else:
            print("Have a good day ahead!!")
            break
    except Exception:
        print("Your mail was not \"Sent\" due to some potential errors...")
        break
