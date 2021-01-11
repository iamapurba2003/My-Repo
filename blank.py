# Employee = {'name':'John', 'Salary':12500, 'age': 23, 'dept':'Production'}
# print("All Elements of the Dictionary -Employees")
# print(Employee)
# print()
# print("Keys of Dictionary - Employee: ", end = " ")
# for k in Employee.keys():
#     print(k,end=", ")

# print()
# print("Thank You")


# Employee = {'name':'John', 'Salary':'12500', 'age': '23', 'dept':'Production'}
# value = Employee.values()
# print("All Elements of the Dictionary - Employee")
# print(Employee)
# print()
# print("Values of Dictionary - Employee: ",end=" ")
# print(", ".join(value))

# print()
# print("Thank You")

"""
Q.8.Write a program in python to print the following series :

X1+ X2 + X3 + …………………..+Xn
"""


# input1 = int(input("Enter number: "))
# extend = int(input("Enter iterable value: "))
# sum = 0
# for i in range(1, extend+1):
#     sum = sum + pow(input1,i)

# print(sum)

"""
 Q.9.Write a program in python to print the following series :

 1^1+ 5^5 + 10^10 + …………………..+N^N
"""
# range1 = int(input("Enter range: "))
# sum = pow(1,1)
# for i in range(0, range1):
#     func = i*5
    
#     sum = sum + pow(func,func)

# print(sum-1)

"""
Q.10.Write a program in python to print the following series :

1/x^1 + 2/x^2 + 3/x^3 + …………………..+N/x^N
"""

# extend = int(input("Enter iterable value: "))
# sum = 0
# for i in range(1, extend+1):
#     m = i/pow(extend,i)
#     sum = sum + m

# print(sum)


"""
Q.11.Write a program in python to print the following series :

1! + 2! + 3! + …………………..+N!
"""

# user_input = int(input("Enter number: "))
# sum = 0
# fact = 1
# for i in range(1,user_input+1):
#     fact *=i
#     sum += fact
# print(sum)



"""
Q.12. Write a program in python to print factorial of a number given by user.
"""

# user_num = int(input("Enter number: "))
# fact = 1
# for i in range(1, user_num+1):
#     fact*=i
# print(fact)

"""
Q.13. Write a program in python to check whether a user given number is an Armstrong number or not.
"""

# num_input = int(input("Enter number: "))
# m = num_input
# sum = 0
# temp = num_input
# count = 0
# while num_input!=0:
#     num_input//=10
#     count = count+1
# for i in range(0, count):
#     num =temp%10
#     sum = sum + pow(num,count)
#     temp//=10
# if sum != m:
#     print("The entered number is not an Armstrong Number.")
# else:
#     print("The entered number is an Armstrong Number.")



"""
Q.14. Write a program in python to print Fibonacci series upto N terms given by user
"""

"""Using .join() where all the elements in the list are <class str>"""
# num_input = 6
# first_term = 0
# scnd_term = 1
# list1 =['0', '1']
# for i in range(0,num_input-2):
#     thrd = scnd_term+ first_term
#     first_term = scnd_term
#     scnd_term = thrd
#     list1.append(str(thrd))
# print(f"The fibonacci Series upto {num_input}th is:", end =" ")
# print(*list1, sep = ", ")
# #print(", ".join(list1))

"""Unpacking the list where all the elements in the list are <class int>"""

# num_input = 6
# first_term = 0
# scnd_term = 1
# list1 =[0, 1]
# for i in range(0,num_input-2):
#     thrd = scnd_term+ first_term
#     first_term = scnd_term
#     scnd_term = thrd
#     list1.append(thrd)
# print(f"The fibonacci Series upto {num_input}th is:", end =" ")
# print(*list1, sep = ", ")

















