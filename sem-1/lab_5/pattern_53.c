#include <stdio.h>
int main()
{
    int n = 4;
    int row,col;
    int count = 2;
    int count1 = 1;
    for(row = 1; row <= n; row++)
    {
        for(col = 1; col <= n-row; col++)
        {
            printf(" ");
        }
        for(col = 1; col <= row; col++)
        {
            printf("*");
            if(row == n-1)
            {
               count = count + 1; 
            }
        }
        for(col = row-1; col >=1; col--)
        {
            printf("*");
        }
        printf("\n");
    }


    //-------------------------------
    for(row = count; row > 0; row = row-2)
    {
        for(int i = 1; i <= count1; i++)
        {
            printf(" ");
        }
        for(col = 1; col <= row; col++)
        {
            printf("*");
        }
        printf("\n");
        count1++;
    }
    return 0;
}