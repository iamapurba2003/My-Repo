import mysql.connector as mc
import stdiomask as iomask

def login(hostname:str, mainuser:str, password:str, key:bool=True)-> None:
    try:
        if key == True:
            db=mc.connect(host=hostname, user=mainuser, passwd=password)
            print(f'========WELCOME TO MySQL Server=======\n{mainuser}@{hostname}!')
            mainCursor=db.cursor()
            stopper= ''
            while True:
                stopper = input('[{}@{}] Enter SQL command> '.format(mainuser, hostname))
                if stopper.casefold() != 'exit':
                    try:
                        mainCursor.execute(stopper)
                        for item in mainCursor:
                            print(item)
                    except Exception as e:
                        print(e)
                
                else:
                    print('Bye')
                    break
        
        else:
            pass
    except Exception as err:
        print(err)


loginhost = input('Enter host of SQL server: ')
username = input('Enter your username in SQL: ')
userpasswd = iomask.getpass(prompt='Enter \'{}\'@\'{}\' password for SQL login: '.format(username, loginhost), mask='*')
oneLiner = f'Connection Host: {loginhost}\nUsername: {username}'
validate = input(f'{oneLiner}\nIs this ok?[y/N]: ')
if validate == 'y'.casefold():
    login(loginhost, username, userpasswd,key=True)

else:
    print('Aborted')

