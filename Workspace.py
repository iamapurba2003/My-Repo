# list1 = [65,45,65,57,82,33,99,44]
# largest = list1[0]
# second_largest = list1[0]
# smallest = list1[0]
# for num in list1:
#     if num>second_largest and num<largest:
#         second_largest = num

#     if num >largest:
#         largest = num



# print(f"The largest number is: {largest}")
# print(f"The second largest number is: {second_largest}")
# # print(f"The smallest number is: {smallest}")


# from Functions import palindrome
# palindrome(101)

# from Functions import *
# user = int(input("Choose one:\n1. Word Palindrome\n2. Number Palindrome\n"))

# if user == 1:
#     str1 = input("Enter word: ")
#     ab = palindrome_str(str1)
#     if ab == True:
#         print(f'Goodluck')
    
# if user == 2:
#     num1 = int(input("Enter number: "))
#     ac = palindrome_num(num1)
#     if ac == True:
#         print(num1/2)



# print("Hello World!")
# print("Welcome to the World of Programming...!")


# import mysql.connector


# db = mysql.connector.connect(user = "root", password = "root", host = "localhost", database = "test", auth_plugin = "mysql_native_password")

# mycursor = db.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(155), address VARCHAR(155))")
# # mycursor.execute("SHOW TABLES")

# # db.commit()

# for x in mycursor:
# 	print(x)


"""Print the following output:
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
23
456
78910"""

# print("Solution to Q5")
# for i in range(1,6):
# 	for j in range(1, i+1):
# 		print(j, end = " ")

# 	print()

"""
Find out the greatest and smallest numbers among three numbers.
"""




def comparison_three_num(x: str = "0, 0, 0"):
	list_num = x.split(", ")
	print(list_num)
	
	smallest = greatest = float(list_num[0])

	for item in list_num:
		if float(greatest) < float(item) :
			greatest = float(item)
			
		
		if float(item) < float(smallest):
			smallest = float(item)
			
	
	print("The greatest number is:", greatest)
	print("The smallest number is:", smallest)


user_num = input("Enter 3 numbers: ")
comparison_three_num(user_num)


















