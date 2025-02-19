num = int(input("Enter number to find factorial: "))
factorial = 1
while num > 1:
    factorial =  factorial * num
    num = num - 1
print("Factorial =",factorial)