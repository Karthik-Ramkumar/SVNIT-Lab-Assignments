#include <stdio.h>
int main()
{
    int a[10];
    int i, j;
    int odd = 0;
    int even = 0;
    printf("enter 10 numbers \n");

    for (i = 0; i < 10; i++)
    {
        scanf("%d", &a[i]);
    }

    for(j = 0; j < 10; j++)
    {
        if(a[j]%2 == 0)
        {
            even++;
        }

        else
        {
            odd++;
        }
    }   
    
    printf(" number of odd numbers = %d", odd);
    printf(" number of even numbers = %d", even);
    return 0;
    
}