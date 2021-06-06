import mysql.connector as mc
import stdiomask as mask
host = input('Enter host name: ')
user = input("Enter your SQL username: ")
passwd = mask.getpass(prompt='Enter your SQL password: ', mask='•')

def main(mainhost='localhost', usermain=..., passwdmain=...) -> list:

    db = mc.connect(host=mainhost, user=usermain, passwd=passwdmain)

    mainCursor = db.cursor()

    mainCursor.execute('show databases')

    return list(datum for datum in mainCursor)


print(main(mainhost=host,usermain=user, passwdmain=passwd))

print("Hello this line is written using VI Text Editor!")
print('Happy Coding!')



