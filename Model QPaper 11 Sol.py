'''Chp Loop, condition and jump statement'''
"""
Q1. Print the following output:
i)
*
**
***
****
*****

ii)
	*
   * *
  * * * 
 * * * *

iii)
 	*
   **
  ***
 ****
*****

iv) 
1
12
123
1234
12345

v)
1
2 3
4 5 6
7 8 9 10

(vi) 
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
# # Solution to 1 i)
# n = int(input("Enter the Number of Rows: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print('*',end=" ")
#     print()

# # Solution to 1 ii)
# n = int(input("Enter the Number of rows: "))
# spaces=n
# for i in range(0,n):
#     for j in range(spaces-1,0,-1):
#         print(" ",end="")
#     for m in range(i+1):
#         print("*",end=" ")
#     print()
#     spaces-=1

# # Solution to 1 iii)
# n = int(input("Enter the Number of Rows: "))
# spaces = n-1
# k = n 
# for i in range(0,n):
#     print(" "*(spaces+n),end=" ")
#     for j in range(k,n+1):
#         print('*',end=" ")
#     spaces-=2
#     k -= 1
#     print()

# # Solution to 1 iv)
# n = int(input("Enter number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end = " ")
#     print()

# # Solution to 1 v)
# n =int(input("Enter number of rows: "))
# for i in range(1,n+1):
#     for j in range(1,i+1 ):
#         print(i, end = ' ')
#     print()















"""
Q2. Fibonacci Series
"""

# userInput = int(input("Enter series range: "))
# a = 0
# b = 1

# list1 = []
# list1.extend([a,b])
# for i in range(0, userInput-2):
#     c = a+b
#     a = b
#     b = c
#     list1.append(c)

# print("The fibonacci series upto {} is:".format(userInput))
# print(*list1,sep=", ")


"""
Q.3.Factorial
"""


# userNum = int(input("Enter number: "))
# fact = 1
# for i in range(1, userNum+1):
#     fact*=i
# print(f"The factorial of {userNum} is {fact}")



'''
Q.4.Series:
(i) 1! , 2!, 3! , ..................n!
(ii) 1^1, 2^2, 3^3, ...............n^n
(iii)1^1/1!  , 2^2/2! , 3^3/3! , ...............n^n/n!
'''

# #Solution to 4 i)
# user_input = int(input("Enter range: "))
# listFact =[]
# fact = 1
# for i in range(1,user_input+1):
#     fact *= i
#     listFact.append(fact)
# print(*listFact,sep=", ")

# #Solution to 4 ii)
# range1 = int(input("Enter range: "))
# listRange =[]
# for i in range(1, range1+1):
       
#     listRange.append(pow(i,i))

# print(*listRange,sep=', ')


#Solution to 4 iii)
# range1 = int(input("Enter range: "))
# listRange =[]
# fact = 1
# a = 0
# for i in range(1, range1+1):
#     a = pow(i,i)
#     fact *= i
#     listRange.append(a/fact)

# print(*listRange, sep=', ')



"""
Q.9.LCM
"""

# def GCD(x: int, y: int):
#     num1 = x
#     num2 = y
#     num3 = 0
#     if num1>num2:
#         while num2 != 0:
#             num3 = num1%num2
#             num1 = num2
#             num2 = num3
#         print(f"The GCD of {x} and {y} is: {num1}")
#         return num1
#     if num2>num1:
#         while num1 != 0:
#             num3 = num2%num1
#             num2 = num1
#             num1 = num3
#         print(f"The GCD of {x} and {y} is: {num2}")
#         return num2

# user_num = input("Enter two numbers: ")
# list_num = user_num.split(", ")
# hcf = GCD(int(list_num[0]),int(list_num[1]))
# multi_nums = int(list_num[0])*int(list_num[1])
# lcm = multi_nums/hcf
# print(f"The LCM of {list_num[0]} and {list_num[1]} is {lcm}")





"""
Q.10.GCD
"""

# def GCD(x: int, y: int):
#     num1 = x
#     num2 = y
#     num3 = 0
#     if num1>num2:
#         while num2 != 0:
#             num3 = num1%num2
#             num1 = num2
#             num2 = num3
#         print(f"The GCD of {x} and {y} is: {num1}")
#         return num1
#     if num2>num1:
#         while num1 != 0:
#             num3 = num2%num1
#             num2 = num1
#             num1 = num3
#         print(f"The GCD of {x} and {y} is: {num2}")
#         return num2


# user_num = input("Enter two numbers: ")
# list_num = user_num.split(", ")
# GCD(int(list_num[0]),int(list_num[1]))













"""Chapter STRING"""
"""
Q1 Palindrome Test
"""

# user_string = input("Enter string: ")

# list_str = user_string.split(" ")

# length = len(list_str)

# joiner = ""

# for i in range(length,-1):
#     joiner = list_str[i] + list_str[i]
    
# rev_joiner = joiner[::-1]
# if rev_joiner.casefold() == joiner.casefold():
#     print(f"\"{user_string}\" is a Palindrome String")
# else:
#     print(f"{user_string} is not a Palindrome String")


"""
Q2 Display even position elements from a user input.
"""

# user_string = input("Enter string: ")

# length = len(user_string)
# print("The even position elements are: ")
# list1 =[]
# for i in range(0, length):
#     if i%2 == 0:
#         list1.append(user_string[i])
#     else:
#         continue

# print(*list1, sep=", ")


"""
Q3 Swap even position characters with its odd position character in a string
"""

string = "String"
temp1 = list(string)
temp = list(string)
length = len(string)
for i in range(0, length):
    if i%2 == 0:     
        temp[i] = temp1[i+1]
    if i%2 !=0:
        temp[i] = temp1[i-1]

print("After swapping the even position characters with its adjacent odd characters...")
print(*temp,sep = "")


"""
Q4. Reverse and dislplay a string using loop
"""

# string = "String"
# temp = ""
# length = len(string)-1
# for i in range(length, -1, -1):
#     temp = temp + string[i]
# print(f"The original string is: \"{string}\"\nThe reversed string is \"{temp}\"")


"""
Q.6. Find no. of words in a sentence given by user using loop
"""

# user_string = input("Enter Sentence: ")
# list_word = user_string.split(" ")
# count =0



# for num in (list_word):
#     count+=1
  
# print(f"The number of words present in the sentence is {count}")


"""
Q7. Find no. of lines in a paragraph using loop.
"""

# user_input = input("Enter paragraph: ")
# list_line = user_input.split(". ")

# count = 0
# for items in list_line:
#     count += 1
# print("The number of lines in the paragraph is: {}".format(count))


"""
Q8. Find no. of vowels in a string(sentence) given by user using loop.
"""

# user_input = input("Enter sentence: ")
# count = 0
# for items in user_input:
#     if items.casefold() in "aeiou":
#         count += 1
# print("The number of vowels in the sentence is: {}".format(count))

"""
Q9. Find no. of uppercase and lowercase alphabets in a string given by user using loop.
"""

# user_input = input("Enter string: ")
# count_low = 0
# count_up = 0
# for i in range(len(user_input)):
#     if user_input[i].isupper() == True:
#         count_up += 1
    
#     if user_input[i].islower() == True:
#         count_low += 1
    
# print("The no. of uppercase alphabets is {}\nThe no. of lowercase alphabets is {}".format(count_up, count_low))


"""
Q10. Find no. of digits in a string given by user using loop.
"""

# user_input = input("Enter string including AlphaNumeric: ")
# count = 0
# for nums in range(len(user_input)):
#     if user_input[nums] in "0123456789":
#         count += 1
    
# print("The no. of digits in the input is: {}".format(count))



"""
Q11. Convert uppercase letter into lowercase letter and vice-versa in a string given by user.
"""

# user_input = input("Enter string: ")
# temp = ""

# for letters in range(len(user_input)):
#     if user_input[letters].isupper() == True:
#         temp = temp + user_input[letters].lower() 
    
#     elif user_input[letters].islower() == True:
#         temp =temp + user_input[letters].upper() 
    
#     else:
#         temp = temp + user_input[letters]
# print("After converting the string you've entered is: \"{}\"".format(temp))


"""
Q12. Convert first letter of every words in a string(sentence-given by user) into uppercase letter.
"""
# user_input = input("Enter sentence: ")
# print("You entered: {}".format(user_input))
# print()
# print("The string after capitalising first letter of every word: {}".format(user_input.title()))
# print()



"""Chapter Lists"""

"""
Q1. Reverse elements of a list using a loop.
"""

# list1 = ['a', 'b', 1, 2, 'c', 'd', 3, 4]
# list2 = []
# for i in range(len(list1)-1, -1,-1):
#     list2.append(list1[i])

# print(list2)

"""
Q2.  Swap even position character with its adjacent odd position character in a list given by user
"""

# userList = eval(input("Enter a list: "))
# listCopy = []

# length = len(userList)

# for i in range(0, length):
#     listCopy.append(userList[i])
#     if i%2 == 0:
#         userList[i] = userList[i+1]
#     if i%2 != 0:
#         userList[i]= listCopy[i-1]

# print(userList)





















