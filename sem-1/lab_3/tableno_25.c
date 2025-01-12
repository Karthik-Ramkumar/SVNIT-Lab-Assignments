#include <stdio.h>
int main()
{
    float input,multi;
    printf("enter number for multiplication table\n");
    scanf("%f",&input);
    int i = 1;
    while(i<=10)
    {
        multi = input*i;
        printf("%f * %d = %f\n",input,i,multi);
        i++;
    }
    return 0;
}