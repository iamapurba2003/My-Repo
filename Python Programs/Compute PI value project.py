range_user = int(input("Enter decimal places of the pi: "))

Denominator = 1

sum = 0

for i in range(1000000):
    if i%2 == 0:
        sum = sum + 4/Denominator
    else:
        sum = sum - 4/Denominator
    
    Denominator+=2


str1 = str(f"{sum:.100f}")
print(str1[range_user])
