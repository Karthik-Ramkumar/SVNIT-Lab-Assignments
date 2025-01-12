#include <stdio.h>

int main() 
{
    int i, j, k, n = 4; 

    for (i = 1; i <= n; i++) 
    {
        // Print leading spaces
        for (j = 1; j <= n - i; j++) 
        {
            printf(" ");
        }

        // Print ascending numbers
        for (k = 1; k <= i; k++) 
        {
            printf("%d", k);
        }

        // Print descending numbers
        for (k = i - 1; k >= 1; k--) 
        {
            printf("%d", k);
        }

        // Move to the next line
        printf("\n");
    }

    return 0;
}
