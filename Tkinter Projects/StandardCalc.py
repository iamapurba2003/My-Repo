from tkinter import *

app = Tk()
app.title("StandardCalc")
numList = []
operatorsList = []
mainState = 1
app.geometry('381x316')
app.resizable(0,0)

calcArea = Entry(app, width=18,borderwidth=5, font=('Arial',28), background="#adb5bd")
calcArea.pack(side=TOP, anchor=NW, fill=X)
calcArea.insert(END,"0")

scroller = Scrollbar(app,orient=HORIZONTAL, command=calcArea.xview)
scroller.pack(side=TOP, anchor=NW, fill=X)
calcArea['xscrollcommand'] = scroller.set

ButtonsFrame = Frame(app)
ButtonsFrame.pack(side=BOTTOM, anchor=SW)
ButtonColor = "#90d9ad"
OperatorColor = "#7fe5f0"
DisabledColor = "#ff0000"
ReadonlyBack = "#adb5bd"
buttonFont = ('Arial',14)

firstNumber = 0

def enableButton():
    Num0.config(state=NORMAL)
    Num1.config(state=NORMAL)
    Num2.config(state=NORMAL)
    Num3.config(state=NORMAL)
    Num4.config(state=NORMAL)
    Num5.config(state=NORMAL)
    Num6.config(state=NORMAL)
    Num7.config(state=NORMAL)
    Num8.config(state=NORMAL)
    Num9.config(state=NORMAL)
    Num0.config(state=NORMAL)
    DelButton.config(state=NORMAL)
    clearButton.config(state=NORMAL)
    SumButton.config(state=NORMAL)
    ProdButton.config(state=NORMAL)
    DiffButton.config(state=NORMAL)
    DivButton.config(state=NORMAL)




def numInput(number: str):
    global mainState
    if calcArea.get() == "0" or mainState==0:
        calcArea.config(state=NORMAL)
        calcArea.delete(0,END)
        calcArea.insert(0, number)
        

    elif calcArea.get() in "+-*/":
        calcArea.config(state=NORMAL)
        calcArea.delete(0, END)
        calcArea.insert(END, number)
        
    
    else:
        calcArea.config(state=NORMAL)
        calcArea.insert(END, number)
        
    enableButton()   
    mainState = 1

def operation(opr="none"):
    if calcArea.get() not in "+-*/":
        numList.append(eval(calcArea.get()))
        print(numList)
    if calcArea.get() in "+-*/":
        operatorsList.pop()

    calcArea.config(state=NORMAL)
    calcArea.delete(0, END)
    if opr == "add":
        operatorsList.append(opr)
        calcArea.delete(0, END)
        calcArea.insert(END, "+")
        SumButton.config(state=DISABLED, disabledforeground=DisabledColor)
        ProdButton.config(state=NORMAL)
        DiffButton.config(state=NORMAL)
        DivButton.config(state=NORMAL)

    elif opr=="diff":
        operatorsList.append(opr)
        calcArea.delete(0, END)
        calcArea.insert(END, "-")
        SumButton.config(state=NORMAL)
        ProdButton.config(state=NORMAL)
        DiffButton.config(state=DISABLED, disabledforeground=DisabledColor)
        DivButton.config(state=NORMAL)
    
    elif opr == "prod":
        operatorsList.append(opr)
        calcArea.delete(0, END)
        calcArea.insert(END, "*")
        SumButton.config(state=NORMAL)
        ProdButton.config(state=DISABLED, disabledforeground=DisabledColor)
        DiffButton.config(state=NORMAL)
        DivButton.config(state=NORMAL)
    
    elif opr == "div":
        operatorsList.append(opr)
        calcArea.delete(0, END)
        calcArea.insert(END, "/")
        SumButton.config(state=NORMAL)
        ProdButton.config(state=NORMAL)
        DiffButton.config(state=NORMAL)
        DivButton.config(state=DISABLED, disabledforeground=DisabledColor)

    
    DecimalPoint.config(state=NORMAL)
    print(operatorsList)

    
def Del():
    calcArea.config(state=NORMAL)
    length = len(calcArea.get())
    calcArea.delete(first=length-1)
    
    enableButton()
    if "." not in calcArea.get():
        DecimalPoint.config(state=NORMAL)


def floatPoint():
    if calcArea.get() in "+-*/":
        operatorsList.append(calcArea.get())
        calcArea.config(state=NORMAL)
        calcArea.delete(0)
        calcArea.insert(END, "0.")
        DecimalPoint.config(state=DISABLED, disabledforeground=DisabledColor)
        
    else:
        calcArea.config(state=NORMAL)
        calcArea.insert(END, ".")
        DecimalPoint.config(state=DISABLED, disabledforeground=DisabledColor)
        


def equal():
    global mainState
    global operatorsList
    global numList
    calcArea.config(state=NORMAL)
    if calcArea.get() not in "+-*/":
        numList.append(eval(calcArea.get()))
    print(numList)
    if len(operatorsList) == len(numList):
        operatorsList.pop()
        for oprs in operatorsList:
            for i in range(len(numList)):
                if oprs == "add":
                    value = numList[0] + numList[1]
                    numList.pop(0)
                    numList.pop(0)
                    numList.insert(0, value)
                    break
                elif oprs == "diff":
                    value = numList[0] - numList[1]
                    numList.pop(0)
                    numList.pop(0)
                    numList.insert(0, value)
                    break
                elif oprs == "div":
                    try:
                        value = numList[0] / numList[1]
                        numList.pop(0)
                        numList.pop(0)
                        numList.insert(0, value)
                        break
                    except ZeroDivisionError:
                        numList.clear()
                        numList.append("ERROR")
                        break
                elif oprs == "prod":
                    value = numList[0] * numList[1]
                    numList.pop(0)
                    numList.pop(0)
                    numList.insert(0, value)
                    break
                
                else:
                    break
    
    else:
        for oprs in operatorsList:
            for i in range(len(numList)):
                if oprs == "add":
                    value = numList[0] + numList[1]
                    numList.pop(0)
                    numList.pop(0)
                    numList.insert(0, value)
                    break
                elif oprs == "diff":
                    value = numList[0] - numList[1]
                    numList.pop(0)
                    numList.pop(0)
                    numList.insert(0, value)
                    break
                elif oprs == "div":
                    try:
                        value = numList[0] / numList[1]
                        numList.pop(0)
                        numList.pop(0)
                        numList.insert(0, value)
                        break
                    except ZeroDivisionError:
                        numList.clear()
                        numList.append("ERROR")
                        break
                elif oprs == "prod":
                    value = numList[0] * numList[1]
                    numList.pop(0)
                    numList.pop(0)
                    numList.insert(0, value)
                    break
                
                else:
                    break

    calcArea.delete(0, END)
    if "." in str(numList[0]):
        if ".000" in str(f"{numList[0]:.3f}"):
            calcArea.insert(END, f'={numList[0]:.0f}')
        else:
            calcArea.insert(END, f'={numList[0]:.3f}')
    else:
        calcArea.insert(END, f'={numList[0]}')
    
    mainState = 0
    numList.clear()
    operatorsList.clear()


def clear():
    global numList
    global operatorsList
    numList.clear()
    operatorsList.clear()
    calcArea.config(state=NORMAL)
    calcArea.delete(0,END)
    calcArea.insert(0,"0")
    
    enableButton()
    DecimalPoint.config(state=NORMAL)



# First Num Row
Num1 = Button(ButtonsFrame, text='1', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("1"), font=buttonFont)
Num1.grid(row=0,column=0)

Num2 = Button(ButtonsFrame, text='2', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("2"), font=buttonFont)
Num2.grid(row=0,column=1)

Num3 = Button(ButtonsFrame, text='3', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("3"), font=buttonFont)
Num3.grid(row=0, column=2)

SumButton = Button(ButtonsFrame, text="+", height=2, width=6, bg=OperatorColor, relief=GROOVE, command=lambda:operation("add"), font=buttonFont)
SumButton.grid(row=0,column=3)

DelButton = Button(ButtonsFrame, text="DEL", height=2, width=6, bg=OperatorColor, relief=GROOVE, command=Del, font=buttonFont)
DelButton.grid(row=0, column=4)

# Second Num Row
Num4 = Button(ButtonsFrame, text='4', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("4"), font=buttonFont)
Num4.grid(row=1,column=0)

Num5 = Button(ButtonsFrame, text='5', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("5"), font=buttonFont)
Num5.grid(row=1,column=1)

Num6 = Button(ButtonsFrame, text='6', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("6"), font=buttonFont)
Num6.grid(row=1, column=2)

DiffButton = Button(ButtonsFrame, text="-", height=2, width=6, bg=OperatorColor, relief=GROOVE, command=lambda:operation("diff"), font=buttonFont)
DiffButton.grid(row=1,column=3)

# Third Num Row
Num7 = Button(ButtonsFrame, text='7', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("7"), font=buttonFont)
Num7.grid(row=2,column=0)

Num8 = Button(ButtonsFrame, text='8', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("8"), font=buttonFont)
Num8.grid(row=2,column=1)

Num9 = Button(ButtonsFrame, text='9', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("9"), font=buttonFont)
Num9.grid(row=2, column=2)

DivButton = Button(ButtonsFrame,text="/", height=2, width=6, bg=OperatorColor, relief=GROOVE, command=lambda:operation("div"), font=buttonFont)
DivButton.grid(row=2, column=3)

# Fourth Num Row
DecimalPoint = Button(ButtonsFrame, text=".", height=2, width=6, bg=ButtonColor, relief=GROOVE, command=floatPoint, font=buttonFont)
DecimalPoint.grid(row=3,column=0)

Num0 = Button(ButtonsFrame, text='0', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=lambda: numInput("0"), font=buttonFont)
Num0.grid(row=3, column=1)

clearButton = Button(ButtonsFrame, text='CLR', height=2, width=6, bg=ButtonColor, relief=GROOVE, command=clear, font=buttonFont)
clearButton.grid(row=3, column=2)

ProdButton = Button(ButtonsFrame, text="*", height=2, width=6, bg=OperatorColor, relief=GROOVE, command=lambda: operation("prod"), font=buttonFont)
ProdButton.grid(row=3,column=3)

EqualButton = Button(ButtonsFrame, text="=", height=2, width=6, bg=OperatorColor, relief=GROOVE, command=equal, font=buttonFont)
EqualButton.grid(row=3,column=4)


app.mainloop()
