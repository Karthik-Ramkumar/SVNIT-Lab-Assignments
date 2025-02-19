import math

def isFibo(n):
    x1 = 5 * n * n + 4
    x2 = 5 * n * n - 4

    if math.isqrt(x1) ** 2 == x1 or math.isqrt(x2) ** 2 == x2:
        return 1
    else:
        return 0

def main():
    n = int(input("Enter how many numbers: "))
    flag_store = []
    for i in range(n):
        num = int(input("Enter number"))
        flag = isFibo(num)
        flag_store.append(flag)
    
    for i in range(len(flag_store)):
        if flag_store[i] == 0:
            print("IsNotFibo")
        else: 
            print("IsFibo")

main()

