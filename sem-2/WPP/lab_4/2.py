import math
cases = int(input("Enter number of cases"))
for i in range(cases):
    low = int(input("Enter lower limit: "))
    high = int(input("Enter higher limit: "))
    temp = low
    count = 0
    while temp <= high:
        if math.sqrt(temp).is_integer():
            count += 1
        temp += 1
    print(count)

        
