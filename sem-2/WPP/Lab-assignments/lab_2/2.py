n=int(input("how many times you want to enter product ? "))
market={}
for i in range(n):
    product=input("enter product : ")
    price=int(input("enter price : "))
    market[product]=price
while(i!=0):
    
    i=int(input("enter 1 for continuing and 0 for exiting "))
    k=input("enter product name ")
    print("price :",market[k])  