names = []
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name of student: ")
    if len(name) <= 15:  
        names.append(name)

for name in names:
    print(name[::-1], end=" ")
