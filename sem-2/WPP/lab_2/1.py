word=input("enter a word : ")
newword=''
for i in range(0,len(word)):
    if(i%2==0):
        
        newword+=word[i]
    
    else:
      
     newword+=word[i].upper()
print(newword)