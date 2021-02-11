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



# for num in range(list_word):
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
# print("The string you've entered is \"{}\"".format(temp))


"""
Q12. Convert first letter of every words in a string(sentence-given by user) into uppercase letter.
"""
# user_input = input("Enter sentence: ")
# print("You entered: {}".format(user_input))
# print()
# print("The string after capitalising first letter of every word: {}".format(user_input.title()))
# print()










