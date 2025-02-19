time=int(input("how many times to enter input "))
while(time!=0):
    count=0
    num=input("enter the number")
    for j in str(num):
        if(int(j)!=0 and int(num)%int(j)==0):
            count+=1
    print(count)
    time-=1