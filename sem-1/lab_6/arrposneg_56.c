#include <stdio.h>
int main()
{
    int a[10];
    int i, j;
    int pos = 0;
    int neg = 0;
    int zero = 0;
    printf("enter 10 numbers \n");

    for (i = 0; i < 10; i++)
    {
        scanf("%d", &a[i]);
    }
//-------------------------------------
    for(j = 0; j < 10; j++)
    {
        if(a[j] < 0)
        {
            neg++;
        }

        else if(a[j] > 0)
        {
            pos++;
        }

        else 
        {
            zero++;
        }
    }   

    printf(" number of positive numbers = %d \n", pos);
    printf(" number of negative numbers = %d \n ", neg);
    printf(" number of zeros  =  %d \n", zero);

}