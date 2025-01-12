#include <stdio.h>
int main()
{
   int input,factorial = 0;
   printf("enter your number to find factorial\n");
   scanf("%d",&input); 
   factorial = input;
   while(input>1)
   {
    input--;
    factorial = factorial*input;
   }
   printf("factorial of your number is = %d\n",factorial);
   return 0;
}
