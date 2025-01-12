#include <stdio.h>

int main() 
{
    int i, j;
    int n = 5; // Number of rows

    for (i = 0; i < n; i++) 
    {
        for (j = 0; j < n; j++) 
        {
            if (j == n - i - 1) 
            {
                printf("1");
            } else 
            {
                printf("0");
            }
        }
        printf("\n");
    }

    return 0;
}
