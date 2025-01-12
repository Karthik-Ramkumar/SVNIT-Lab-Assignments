#include <stdio.h>
int main()
{
    int input =0;
    int count = 0;
    printf("enter number\n");
    scanf("%d",&input);
    int store = input;
    //----------------------------------
    while(input>0)
    {
        int remainder = input%10;
        if(store% remainder == 0)
        {
            count++;
        }
        input = input/10;
    }
    printf("%d",count);
    return 0;
}