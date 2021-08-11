#------------------------------- Global Variables -------------------------------------#
import time
BOLD = '\u001b[1m'
RESET = '\u001b[0m'
UNDERLINE = '\u001b[4m'


def Grader(score : int):
    if score >= 91:
        return "A+"
    if score >= 81 and score <= 90:
        return "A"
    if score >= 71 and score <= 80:
        return "B+"
    if score >= 61 and score <= 70:
        return "B"
    if score >= 51 and score <= 60:
        return "C"
    if score >= 41 and score <= 50:
        return "D"
    if score >= 31 and score <= 40:
        return "E"
    if score <= 30:
        return "Fail"


def percentage (x : int): 
    percentage = (x/600)*(100)
    return percentage



def ReportCard(*args : tuple, screenwidth : int = 64):
    sum = int(args[6][0]) + int(args[6][1]) + int(args[6][2]) + int(args[6][3]) + int(args[6][4]) + int(args[6][5])
    percent = percentage(sum)
    counter = 1
    while counter <= 41:
        if counter == 1 or counter == 6 or counter == 41:
            print('~'*(screenwidth+2))
            counter += 1
            continue
        
        if counter == 3:
            container = "Annual Report Card of Student 2020-2021"
            print(f"|{BOLD}{container.center(screenwidth)}{RESET}|")
            counter += 1
            continue
        
        if counter == 4:
            if counter == 4:
                container = "KV Ranaghat"
                print(f"|{BOLD}{container.center(screenwidth)}{RESET}|")
            counter += 1
            continue
        
        if counter == 8:
            container = "General Info of Student"
            print(f"|{BOLD}{container.center(screenwidth)}{RESET}|")
            counter += 1
            continue
        
        if counter == 10:
            text = f"Name: \t\t{args[0]}"
            data = text.ljust(screenwidth-7," ")
            print(f"|{data}|")
            counter += 1
            
        if counter == 11:
            text = f"Class: \t{args[1]}"
            data = text.ljust(screenwidth-7, " ")
            print(f"|{data}|")
            counter += 1
            
        if counter == 12:
            text = f"Section: \t{args[2]}"
            data = text.ljust(screenwidth-5, " ")
            print(f"|{data}|")
            counter += 1
            
        if counter == 13:
            text = f"Roll Number: \t{args[3]}"
            data = text.ljust(screenwidth-1, " ")
            print(f"|{data}|")
            counter += 1
            
        if counter == 14:
            text = f"Department: \t{args[4]}"
            data = text.ljust(screenwidth-2, " ")
            print(f"|{data}|")
            counter += 1
        
        if counter == 16:
            container = "Marks Obtained:"
            print(f"|{BOLD}{container.ljust(screenwidth,' ')}{RESET}|")
            counter += 1
        
        if counter == 18:
            container = "Subject                    Marks                      Grade"
            print(f"|{BOLD}{container.ljust(screenwidth,' ')}{RESET}|")
            counter += 1
        
        if counter == 20:
            container = f"{args[5][0]}                {args[6][0]}                          {args[7]}"
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 21:
            container = f"{args[5][1]}                      {args[6][1]}                         {args[8]}"
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 22:
            container = f"{args[5][2]}                    {args[6][2]}                         {args[9]}"
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 23:
            container = f"{args[5][3]}                      {args[6][3]}                         {args[10]}"
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 24:
            container = f"{args[5][4]}                      {args[6][4]}                         {args[11]}"
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 25:
            container = f"{args[5][5]}               {args[6][5]}                        {args[12]}"
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
        
        if counter == 27:
            container = f"Co-Scholastic Info"
            print(f"|{BOLD}{container.center(screenwidth)}{RESET}|")
            counter += 1
        
        if counter == 29:
            container = f"The Height of the Student is {args[13]} M."
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 30:
            container = f"The Weight of the Student is {args[14]} Kg."
            print(f"|{container.ljust(screenwidth, ' ')}|")
            counter += 1
            
        if counter == 31:
            container = f"The Awards the Student has won (is/are) {args[15]}."
            print(f"|{UNDERLINE}{container.ljust(screenwidth, ' ')}{RESET}|")
            counter += 1
            
        if counter == 32:
            container = f"The Activities the Student has participated in (is/are) {args[16]}."
            print(f"|{UNDERLINE}{container.ljust(screenwidth, ' ')}{RESET}|")
            counter += 1
            
        if counter == 38:
            data = f"Total Marks Obtained is {sum}"
            print(f"|{BOLD}{data.center(screenwidth)}{RESET}|")
            counter += 1
        
        if counter == 39:
            data = f"Percentage Obtained is {percent:.2f}%"
            print(f"|{BOLD}{data.center(screenwidth)}{RESET}|")
            counter += 1
        
            
        else:
            container= " "
            data = f"|{container.center(screenwidth)}|"
            print(data)
            counter += 1   
            continue    
    pass

def main():
    for j in range(1,6):
        if j == 1 or j == 5:
            print("+", "-"*39, "+")
        if j == 3:
            print(f"|{'General Info About Student'.center(41)}|")
    print()
    name = input("Name: ")
    Class = input("Class: ")
    section = input("Section: ")
    rollno = input("Roll No: ")
    dept = input("Department: ")
    subjects = eval(input("""\t Enter Subject names(Seperated by ', ', in list form):   """ ))
    mark = input("""\tEnter Marks of all the Subject: """)
    marks = mark.split(', ')
    print()
    for j in range(1,6):
        if j == 1 or j == 5:
            print("+", "-"*45, "+")
        if j == 3:
            print(f"|{'Co-Scholastic Info of Student'.center(47)}|")
    print()
    height = input("Height: ")
    weight = input("Weight: ")
    awards = input("Awards (if any, not more than 1): ")
    activities = input("Activities Participated (if any, not more than 1): ")
    print()
    print()
    print("""Now Generating Annual Report Card of SURYADUYTI BANERJEE for the Session 2020-2021 of Class 11..... """)
    print()
    grade1 = Grader(int(marks[0]))
    grade2 = Grader(int(marks[1]))
    grade3 = Grader(int(marks[2]))
    grade4 = Grader(int(marks[3]))
    grade5 = Grader(int(marks[4]))
    grade6 = Grader(int(marks[5]))
    time.sleep(2)
    ReportCard(name,Class,section,rollno,dept,subjects,marks,grade1,grade2,grade3,grade4,grade5,grade6,height,weight,awards,activities)
if __name__ == "__main__":
    main()