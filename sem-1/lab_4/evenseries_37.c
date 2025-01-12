#include <stdio.h>
int main()
{
    int input;
    int x = 0;
    printf("enter how long the series should be \n");
    scanf("%d",&input);

    for(int i = 1 ; i <= input;i++)
    {
        printf(" %d",x);
        x = x+2;

    }
    return 0;
}