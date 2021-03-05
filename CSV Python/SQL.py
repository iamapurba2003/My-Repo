import mysql.connector as mc
import csv 
db = mc.connect(host='localhost', user='root', passwd='root', database = 'csv')

fileName = "CSV_Python.csv"

myCursor = db.cursor()

# This part is only for reading a csv file and inserting into a database{

# with open(fileName, 'r') as csvFile:
#     csvReader = csv.reader(csvFile)
#     for line in csvReader:
#         fields = tuple(line)
#         # print(fields)
#         myCursor.execute("insert into students (Name, Class, Section, Roll) values(%s, %s, %s, %s)", fields)
#         db.commit()

#           }

#This part is only for retrieving the queries from a database and conveting it into a csv file.{

# myCursor.execute("select * from students")
# res = myCursor.fetchall()
# with open("newFile1.csv", "w") as newCSVFile:
#     for lines in res:
#         csv.writer(newCSVFile).writerow(lines)

#               }









