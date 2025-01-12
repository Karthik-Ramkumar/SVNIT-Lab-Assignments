#include <stdio.h>

int main() 
{
    int row, col, k;
    int n = 4; // Number of rows

    for (row = 1; row <= n; row++) 
    {
        // Print leading spaces
        for (col = 1; col <= n - row; col++) 
        {
            printf(" ");
        }
        // Print ascending stars
        for (k = 1; k <= row; k++) 
        {
            printf("*");
        }
        // Print descending stars
        for (k = row - 1; k >= 1; k--)
         {
            printf("*");
        }
        // Move to the next line
        printf("\n");
    }

    return 0;
}
