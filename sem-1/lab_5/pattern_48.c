#include <stdio.h>

int main() 
{
    int i, j;
    int n = 4; 

    for (i = 1; i <= n; i++) 
    {
        // Print letters
        for (j = 1; j <= i; j++) 
        {
            printf("%c", 'A' + j - 1);
        }
        // Move to the next line
        printf("\n");
    }

    return 0;
}
