#---------!Modules and others!----------
import time

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'
RESET = '\u001b[0m'

#----------------! General Info about Candidate !-----------------

Session = input("Enter Session: ")
Name = input("Enter Name of the Candidate: ")
Cls = input("Enter Candidate's Class: ")
Sec = input("Enter Candidate's Section: ")
Roll = int(input("Enter Candidate's Roll No.: "))




#----------------! Stream Selection !-------------------
Stream = int(input("Choose Stream:\n1. Science\n2. Commerce\n3. Arts:\n"))
if Stream == 1:
    print()
    subjects = input("Enter 6 subjects' name: ")
    listSub = subjects.split(", ")
    subMarks = input("Enter marks for respective subjects entered: ")
    listMarks = subMarks.split(", ")

if Stream == 2:
    print()
    subjects = input("Enter 6 subjects' name: ")
    listSub = subjects.split(", ")
    subMarks = input("Enter marks for respective subjects entered: ")
    listMarks = subMarks.split(", ")


if Stream == 3:
    print()
    subjects = input("Enter 6 subjects' name: ")
    listSub = subjects.split(", ")
    subMarks = input("Enter marks for respective subjects entered: ")
    listMarks = subMarks.split(", ")



#---------------! Co-Scholastic Area !---------------
# print()
# heightStu = float(input("Enter Height of the Candidate (in meters): "))
# massStu = int(input("Enter Weight of the Candidate (in kilograms): "))
# award = input("Enter awards achieved by the Candidate(if any):")
# participate = input("Enter co-scholastic programmes where Candidate has taken part(if any): ")
# attend = int(input("Enter Attendance of the Candidate(out of 190 days): "))

#-----------! User choice for result !-----------
print()
choiceUser = int(input("1. Continue generating the results\n2. To terminate the Program with time after the report card is generated."))

if choiceUser == 1:
    print()

    def results(u: int = 100, x: float = 5):
        print("{}Annual Report Card for Session {}{}".format(UNDERLINE, Session, RESET))
        print(f'{UNDERLINE}{"Satish Chandra Memorial School".center(20)}{RESET}')
        print()
        print(f'\t{UNDERLINE}{"STUDENT INFORMATION BELOW:"}{RESET}')
        print(f"Name of Candidate: {Name}\nClass and Section: {Cls} {Sec}")
        print(f"Roll Number: {Roll}")
        
        print("Marks in Subjects:")
        print(f"{UNDERLINE}Subjects{RESET}  \t\t{UNDERLINE}Marks{RESET}")
        i = 0
        while i<len(listSub):
            print(listSub[i],listMarks[i].rjust(10))
            i+=1


        
        
    results()






































































