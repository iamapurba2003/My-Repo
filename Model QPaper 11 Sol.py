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

# user_string = "String"

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

# string = "String"

# temp = user_string
# length = len(user_string)-1
# for i in range(0, length):
#     if i%2 == 0:
        
#         temp = temp.replace(user_string[i], user_string[i+1])
    
    
# print(temp)


"""
Q4. Reverse and dislplay a string using loop
"""

string = "String"
temp = ""
length = len(string)-1
for i in range(length, -1, -1):
    temp = temp + string[i]
print(f"The original string is: \"{string}\"\nThe reversed string is \"{temp}\"")


"""
Q.6. Find no. of words in a sentence given by user using loop
"""

user_string = input("Enter Sentence: ")
list_word = user_string.split(" ")
count =0

length = len(list_word)

for num in range(length):
  count+=1
  
print(f"The number of words present in the sentence is {count}")
















