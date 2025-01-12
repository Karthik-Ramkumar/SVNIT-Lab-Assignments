#include<stdio.h>
int main(){
char msg[100];
int count=0,i=0;
gets(msg);
while(i<100)
{
if(msg[i]=='\0')
{
    break;
}
else
{
    count++;
}
i++;
}
printf("length is %d",count);
return 0;
}