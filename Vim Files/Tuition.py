def fibonacci(lastTerm: int = ...)-> list:
	list1 = []
	a = 0
	b = 1
	list1 = [a, b]
	for i in range(0, lastTerm-2):
		c = a + b
		a = b
		b = c
		list1.append(c)
	return list1


inputUser = int(input("Enter last term: "))
print("The fibonacci series upto {} terms".format(inputUser))
print(*fibonacci(inputUser), sep=", ")

