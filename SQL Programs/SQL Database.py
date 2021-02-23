# """
# Write a code to create a database in MySQL
# """

# import mysql.connector 
# db = mysql.connect(host = "localhost", user = "root", password = "root", auth_plugins = "mysql_native_password")
# myCursor = db.cursor()






# """
# Write a Program to Create five tables in the database created in the previous file.
# """

# import mysql.connector 
# db = mysql.connect(host = "localhost", user = "root", password = "root", auth_plugins = "mysql_native_password")
# myCursor = db.cursor()

# Q1 = "CREATE TABLE table1(name VARCHAR(50), class int(5), sec(5))"
# Q2 = "CREATE TABLE table1(name VARCHAR(50), class int(5), sec(5))"
# Q3 = "CREATE TABLE table1(name VARCHAR(50), class int(5), sec(5))"
# Q4 = "CREATE TABLE table1(name VARCHAR(50), class int(5), sec(5))"
# Q5 = "CREATE TABLE table1(name VARCHAR(50), class int(5), sec(5))"

# myCursor.execute(Q1)
# myCursor.execute(Q2)
# myCursor.execute(Q3)
# myCursor.execute(Q4)
# myCursor.execute(Q5)

# db.commit()
# myCursor.execute("SHOW TABLES")
# for x in myCursor:
#     print(x)



# """
# Write a program to insert 5 records in any one of the table created 
# """


# import mysql.connector 
# db = mysql.connect(host = "localhost", user = "root", password = "root", auth_plugins = "mysql_native_password")
# myCursor = db.cursor()

# myCursor.execute("INSERT INTO table1(name,class, sec) VALUES(%s, %s, %s)")
# userData = [
#     ("Apurba Ghosh", 11, "C"),
#     ("Himangshu De", 11, "C"),
#     ("Raima Ray", 11, "B"),
#     ("Priyanka Das", 11, "D"),
#     ("Rupankar Das", 11, "C")
# ]

# #myCursor
# for x in userData:
#     myCursor.execute(Q1, x)

# myCursor.execute("SELECT * FROM table1 OREDER BY sec ASC/DESC ")
# for x in myCursor:
#     print(x)


import mysql.connector as mc

db = mc.connect(host = "localhost", user = "root", password = "root", database = "testimonials")

Cursor = db.cursor()

executer = "DROP TABLE IF EXISTS users"

Cursor.execute(executer)

db.close()

















