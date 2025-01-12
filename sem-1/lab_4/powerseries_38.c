#include <stdio.h>
int main()
{
    int input;
    int x = 1;
    printf("enter how long the series should be \n");
    scanf("%d",&input);

    for(int i = 1 ; i <= input;i++)
    {
        x = i*i;
        printf(" %d",x);


    }
    return 0;
}