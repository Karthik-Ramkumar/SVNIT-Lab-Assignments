
A = int(input("Enter A: "))
B = int(input("Enter B: "))
max = 0

while A <= B:
    atemp = A  
    while atemp <= B:
        if (A ^ atemp) > max:
            max = A ^ atemp
        atemp += 1 
    A += 1  

print(max)
