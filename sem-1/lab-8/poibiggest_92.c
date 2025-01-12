#include <stdio.h>
int main()
{
    int big = 0;
    int *ptr;
    int num[5];
    printf("enter numbers \n");
    for(int i=0;i<5;i++)
    {
        scanf("%d",&num[i]);      
    }
    ptr = num;
    for(int i=0;i<5;i++)
    {
        if(*ptr >big)
        {
            big = *ptr;
        }
        ptr++;
    }
    printf("biggest number = %d",big);
    return 0;
}