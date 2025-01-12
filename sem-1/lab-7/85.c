#include<stdio.h>
#include<string.h>
int main(){
 static int count=0,i=0;
char msg[100];
gets(msg);
for(i=0;i<strlen(msg);i++)
{
switch(msg[i])
{
case 'a':count++;
break;
case 'e':count++;
 break;
case 'i':count++;
 break;
case 'o':count++;
 break;
case 'u':count++;
 break;
}
}

printf("\nno of vowels is %d",count);
return 0;
}