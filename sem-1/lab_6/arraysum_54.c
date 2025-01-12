#include <stdio.h>
int main()
{
    int a[10];
    int i,j;
    printf("enter 10 numbers \n");
    for( i = 0; i <10; i++)
    {
        scanf("%d",&a[i]);
    }
    int sum = 0;
    for(j = 0; j < 10; j++)
    {
        sum = sum + a[j];
    }
    printf("sum of entered numbers = %d \n", sum);
    return 0;

}