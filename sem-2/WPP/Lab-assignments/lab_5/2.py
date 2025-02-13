cuts = int(input("Enter number of cuts"))
if cuts % 2 == 0:
    print(cuts*2)
else:
    print(int(((cuts+1)/2)+((cuts+1)/2)))