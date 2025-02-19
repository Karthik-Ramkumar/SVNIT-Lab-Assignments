# num = input("Enter number to reverse: ")
# rev = reversed(num)
# print(rev)

number = int(input("Enter a number: "))
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)