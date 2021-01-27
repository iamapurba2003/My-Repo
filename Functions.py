from typing import Any


def armstrong(x: int):
    """
    This function determines whether the number given as input is `Armstrong` or not.
    """

    m = x
    sum = 0
    temp = x
    count = 0
    while x!=0:
        x//=10
        count = count+1
    for i in range(0, count):
        num =temp%10
        sum = sum + pow(num,count)
        temp//=10
    if sum != m:
        print("The entered number is not an Armstrong Number.")
    else:
        print("The entered number is an Armstrong Number.")

# a = 1634
# armstrong(a)

def odev(x: int):


    """
    Declares whether a number is `Odd` or `Even` 
    """
    if x%2 !=0:
        print(f'{x} is an Odd number')
    
    else:
        print(f"{x} is an Even Number")

# a = 5
# odev(a)



def comparison(x: list):
    '''
    Gives `Largest` and `Smallest` number from the list specified by user.
    '''
    largest = smallest = x[0]
    for item in x:
        if item>largest:
            largest = item

        if item<smallest:
            smallest = item

    print(f"The largest number is: {largest}")
    print(f'The smallest number is: {smallest}')

# user_list = [105.25, 102.25678, 2, 21, 4000.001, 4001.010001, 505, 101, 5001, 5002.00000012356789, 4024, 3624, 5006.000256]
# print(user_list)
# comparison(user_list)


def Fah_to_Cel(x: float) -> bool:
    """
    Converts `Fahrenheit` measure into `Celsius` measure. 
    """
    C_measure = (x-32)*5/9
    
    print(f"{C_measure:.3f}")
    return True


# p1 = 273
# print(Fah_to_Cel(p1))


def palindrome_str(x: str) -> bool:
    """
    Prints whether a `string` is a `Palindrome` or not.
    """
    
    rev = x[::-1]
    if rev.casefold() == x.casefold():
        print(f"{x} is a Palindrome string.")
        return True
    else:
        print(f"{x} is not a Palindrome string.")
        return False
    
def palindrome_num(x: int) -> bool:
    '''
    Checks whether a `integer number` is a `Palindrome` or not.
    '''
    temp = x
    sum = ''
    while temp !=0:
        sum = sum + str(temp%10)
        temp = temp//10    
    if int(sum) == x:
        print(f'{x} is a Palindrome number.')
        return True
    else:
        print(f'{x} is not a Palindrome number.')
        return False
    

# ab = int(input("Enter character: "))
# palindrome_num(ab)

print("added one line")
