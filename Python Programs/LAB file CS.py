"""Q1. Write a program in python to convert temperature from Fahrenheit to Celsius."""

user_input = float(input("Enter temperature measure in Fahrenheit scale: "))
C_measure = (user_input-32)*5/9
print("The temperature measure in Celsius is", C_measure)



"""Q.2. Write a program in python to convert temperature from Celsius to Fahrenheit"""

user_temp_input = float(input("Enter temp measure in Celsius scale: "))
F_measure = ((user_temp_input*9/5)+32)
print("The temperature measure in Fahrenheit is", F_measure)


""" Q.3.Find out roots of a quadratic equation whose polynomials will be given by user """


from math import *


a = int(input("Enter the Value of A: "))
b = int(input("Enter the Value of B: "))
c = int(input("Enter the Value of C: "))

d = pow(b,2) - (4*a*c)
sum1 = (-b + sqrt(d))/(2*a)
sum2 = (-b - sqrt(d))/(2*a)
print(f"The Roots of the Equation are {sum1} & {sum2}")


"""
Q.4. Write a program in python to generate a report card of a students according to CBSE grade system. User will input 6 subject marks (English, Bengali/Hindi, Physics, Chemistry, Biology and Computer).Find out the total mark and grade. The grade will be calculated as follows:
91-100 – “A+”
81-90 – “A”
71-80 – “B+”
61-70 – “B”
51-60 – “C”
41-50 – “D”
31-40 – “E”
Below 40 – “Fail”
"""


input_xm_total = float(input("Enter full marks of exam: "))
input_eng = float(input("Enter english marks: "))
input_2ndLang = float(input("Enter 2nd Lang. marks: "))
input_Phy = float(input("Enter Physics marks: "))
input_Chem = float(input("Enter Chemistry marks: "))
input_Bio = float(input("Enter biology marks: "))
input_CS = float(input("Enter computer science marks: "))

total_marks = (input_eng) + (input_2ndLang) + (input_Phy) + (input_Chem) + (input_Bio) + (input_CS)
print("Your total marks is", total_marks)
grade = (total_marks/(input_xm_total*6))*100
print("Your percentage is",grade,"%")
if grade >=91  and grade <= 100: 
    print("Your grade is A+")
if grade>=81 and grade <=90:
    print("Your grade is A")
if grade >=71 and grade<= 80:
    print("Your grade is B+")
if grade >=61 and grade <=70:
    print("Your grade is B")
if grade >=51 and grade<=60:
    print("Your grade is C")
if grade >=41 and grade<=50:
    print("Your grade is D")
if grade >= 31 and grade <=40:
    print("Your grade is E")
if grade <=40:
    print("You failed this examination")
    print("Better luck next time")






"""Q.5.Write a program in python to print first 100 even numbers"""

count = 0
for i in range(0,200):
    if i%2 == 0:
      print(i, end = " ")
      if count == 100:
          break
    else:
        continue
    count += 1



"""Q.6. Write a program in python to print all the multiples of 5 from 1 to 100 """


for i in range(1,101):
  if i%5 == 0:
      print(i, end = " ")


"""
Q.7. Write a program in python to print the following series : 
1! + 2! + 3! + …………………..+N!
"""

sum = 0
fact = 1 
input_num = int(input("Enter number: "))
for i in range(1, input_num+1):

    fact = fact*i
    sum += fact
    print(sum) 



"""
Q.8.Write a program in python to print the following series :

X1+ X2 + X3 + …………………..+Xn
"""


input1 = int(input("Enter number: "))
extend = int(input("Enter iterable value: "))
sum = 0
for i in range(1, extend+1):
    sum = sum + pow(input1,i)

print(sum)

"""
 Q.9.Write a program in python to print the following series :

 1^1+ 5^5 + 10^10 + …………………..+N^N
"""
range1 = int(input("Enter range: "))
sum = pow(1,1)
for i in range(0, range1):
    func = i*5
    
    sum = sum + pow(func,func)

print(sum-1)

"""
Q.10.Write a program in python to print the following series :

1/x^1 + 2/x^2 + 3/x^3 + …………………..+N/x^N
"""

extend = int(input("Enter iterable value: "))
sum = 0
for i in range(1, extend+1):
    m = i/pow(extend,i)
    sum = sum + m

print(sum)



"""
Q.11.Write a program in python to print the following series :

1! + 2! + 3! + …………………..+N!
"""

user_input = int(input("Enter number: "))

fact = 1
for i in range(1,user_input+1):
    fact *= i
    sum+=fact
print(sum)


"""
Q.12. Write a program in python to print factorial of a number given by user.
"""

user_num = int(input("Enter number: "))
fact = 1
for i in range(1, user_num+1):
    fact*=i
print(fact)


"""
Q.13. Write a program in python to check whether a user given number is an Armstrong number or not.
"""
num_input = int(input("Enter number: "))
m = num_input
sum = 0
temp = num_input
count = 0
while num_input!=0:
    num_input//=10
    count = count+1
for i in range(0, count):
    num =temp%10
    sum = sum + pow(num,count)
    temp//=10
if sum != m:
    print("The entered number is not an Armstrong Number.")
else:
    print("The entered number is an Armstrong Number.")


"""
Q.14. Write a program in python to print Fibonacci series upto N terms given by user
"""


num_input = 6
first_term = 0
scnd_term = 1
list1 =[0, 1]
for i in range(0,num_input-2):
    thrd = scnd_term+ first_term
    first_term = scnd_term
    scnd_term = thrd
    list1.append(thrd)
print(f"The fibonacci Series upto {num_input}th is:", end =" ")
print(*list1, sep = ", ")


'''
Q.15. Write a program in python to find out GCD of two numbers given by user.
'''

def GCD(x: int, y: int):
    num1 = x
    num2 = y
    num3 = 0
    if num1>num2:
        while num2 != 0:
            num3 = num1%num2
            num1 = num2
            num2 = num3
        print(f"The GCD of {x} and {y} is: {num1}")
        return num1
    if num2>num1:
        while num1 != 0:
            num3 = num2%num1
            num2 = num1
            num1 = num3
        print(f"The GCD of {x} and {y} is: {num2}")
        return num2


user_num = input("Enter two numbers: ")
list_num = user_num.split(", ")
GCD(int(list_num[0]),int(list_num[1]))


"""
Q.16. Write a program in python to find out LCM of two numbers given by user.
"""

def GCD(x: int, y: int):
    num1 = x
    num2 = y
    num3 = 0
    if num1>num2:
        while num2 != 0:
            num3 = num1%num2
            num1 = num2
            num2 = num3
        print(f"The GCD of {x} and {y} is: {num1}")
        return num1
    if num2>num1:
        while num1 != 0:
            num3 = num2%num1
            num2 = num1
            num1 = num3
        print(f"The GCD of {x} and {y} is: {num2}")
        return num2

user_num = input("Enter two numbers: ")
list_num = user_num.split(", ")
hcf = GCD(int(list_num[0]),int(list_num[1]))
multi_nums = int(list_num[0])*int(list_num[1])
lcm = multi_nums/hcf
print(f"The LCM of {list_num[0]} and {list_num[1]} is {lcm}")


"""
Q.17. Write a program in python to print only the even position elements of a list given by user.
"""

user_in = input("Enter elements for list: ")
list_user = user_in.split(",")
print("The list is: ", list_user)
length = len(list_user)
print("The even position elements are: ")
for i in range(length-1):
    if i%2 == 0:
        print(list_user[i+1], sep = ", ")
    else: 
        pass


"""
Q.18. Write a program in python to print a list in reverse order using for loop
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1)
list2 = []
for i in range(len(list1)-1, -1,-1):
    list2.append(list1[i])
print(list2)


"""
Q.19. Write a program in python to search any number within a list. The list and the number to be find out will be given by user.
"""

user_input = input("Enter numbers for adding in list: ")
list1 = user_input.split(", ")
print(list1)
search = int(input("Enter the number you want to search in the list: "))
for i in range(len(list1)):
    if search == int(list1[i]):
        print(f"The number {int(search)} is at position {i+1} in the list")
    else:
        continue


'''
Q.20. Write a program in python to print only the odd numbers from a tuple. The tuple will be given by user.
'''

user_tuple = eval(input("Enter a numeric tuple: "))

length = len(user_tuple)
print(f"The tuple entered by you is: {user_tuple}")
list1 = []
for i in range(0, length):
    if int(user_tuple[i])%2 != 0:
        list1.append(str(user_tuple[i]))
print("The odd numbers from the tuple are:") 
print(*list1,sep=", ")



"""
Q.21. Write a program in python to print a string in reverse order using loop. The string will be given by user.
"""


user_input = input("Enter string: ")
length = len(user_input)
i = length-1
while i!= -1:
    print(user_input[i], end = "")
    i -=1


'''
Q.22. Write a program in python to print even position element and odd position element of a user given string individually.
'''

user_str = input("Enter your string: ")
length = len(user_str)
list_odd = []
list_even = []
for i in range(0, length):
    if i%2 !=0:
        list_odd.append(user_str[i])
    if i%2 ==0:
        list_even.append(user_str[i])
print('The even position string elements are:')
print(*list_odd, sep=", ")
print("The odd position string elements are:")
print(*list_even, sep = ", ")

'''
Q.23.Write a program to print all the keys of a dictionary and all the values of a dictionary individually.
'''

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"The Dictionary is: {dictionary}")
keys = dictionary.keys()
val = dictionary.values()
print("The keys of the dictionary are: ")
print(*keys, sep=", ")
print("The values of the dictionary are: ")
print(*val, sep=", ")

'''
Q.24. Write a program in python to find out the largest and smallest number in an integer list given by user.
'''
'''Original Solution'''

user_list = eval(input("Enter a list: "))
print(user_list)
largest = smallest = user_list[0]
for item in user_list:
    if item>largest:
        largest = item

    if item<smallest:
        smallest = item

    print(f"The largest number is: {largest}")
    print(f'The smallest number is: {smallest}')




'''
Q.25. Write a program in python to find out how many vowels are there in a user given string.
'''


def vowel(x: str):
    '''
    Gives number of `Vowels` present in a `user given` string.
    '''
    length = len(x)

    
    list1 = []
    for i in range(length):
        if x[i].casefold() in 'aeiou':
            list1.append(x[i])
    print(f"The number vowels are present in your input is/are: {len(list1)} and the vowel(s) is/are: ", *list1)

input1 = input("Enter your string: ")
vowel(input1)
