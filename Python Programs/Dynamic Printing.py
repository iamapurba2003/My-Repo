"""
Methods for Dynamic Printing...
"""
# import time
# count =0
# while count <3:
# 	print("\rViewing the Task List.../ ", end="")
# 	time.sleep(0.3)
# 	print("\rViewing the Task List...- ", end="")
# 	time.sleep(0.3)
# 	print("\rViewing the Task List...\ ", end="")
# 	time.sleep(0.3)
# 	print("\rViewing the Task List...| ", end="")
# 	time.sleep(0.3)
# 	print("\rViewing the Task List.../ ", end="")
# 	time.sleep(0.3)
# 	print("\rViewing the Task List...- ", end="")
# 	time.sleep(0.3)

# 	count += 1 



# import pickle
# # f = open("new.dat", "rb")
# fileName = "/home/himangshuishere/Documents/Sample.txt"
# f = open(fileName, "r")
# if ".txt" not in fileName:
# 	reader = pickle.load(f)
# else:
# 	reader = f.read()
# print(reader)


import time
count = 0
# while count < 20:
# 	print("\r lease Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rP ease Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPl ase Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPle se Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlea e Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPleas  Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease  ait... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease W it... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wa t... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wai ... ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wait .. ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wait. . ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wait..  ", end="")
# 	time.sleep(0.1)
# 	print("\rPlease Wait... ", end="")
# 	time.sleep(0.1)

# 	count += 1
# print()
# print("Done!")
# txt = "Please Wait..."
# for i in range(1,20):
#     print("\r"+txt+"/ ", end="")
#     time.sleep(0.1)
#     print("\r"+txt+"- ", end="")
#     time.sleep(0.1)
#     print("\r"+txt+"\ ", end="")
#     time.sleep(0.1)
#     print("\r"+txt+"| ", end="")
#     time.sleep(0.1)
#     print("\r"+txt+"/ ", end="")
#     time.sleep(0.1)
#     print("\r"+txt+"- ", end="")
#     time.sleep(0.1)
    


def dynamicPrinting(__txt:str="None", __times: int= 10, __speed:float = 0.1, __jump:int = 1):
    count = 0
    run= 0
    for i in range(1, __times):
        for items in range(0,len(__txt), __jump):
            text = list(txt)
            text[items] = " "
            text.insert(0,"\r")
            main = text
            print(*main,sep="", end="")
            time.sleep(__speed)
            text.remove("\r")

    print()

txt = input("Enter text to be dynamically printed: ")
times_ = int(input("Enter no. of rounds: "))
speed_ = float(input("Enter speed of animation: "))
jump_ = int(input("Enter total text jump: "))
dynamicPrinting(txt, times_, speed_, jump_)
