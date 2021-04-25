print("This is Untitled-1.py file")
userNumInput = int(input('Enter a number: '))
temp = userNumInput
new = userNumInput
count = 0
sum = 0
while sum != userNumInput:
    while temp !=0:
        temp //= 10
        count += 1
    run = new%10
    sum += pow(run, count)
    new//=10

if sum == userNumInput:
    print("{} is an Armstrong Number!".format(userNumInput))
else:
    print("{} is not an Armstrong Number!".format(userNumInput))
