#include <stdio.h>

int main() 
{
    int i, j;
    char ch;

    for (i = 1; i <= 5; i++) 
    {
        ch = 'A'; // Determine the character to print
        for(j = 1; j <= i; j++) 
        {
            ch = 'A' + j - 1;
            printf("%c", ch);
        }
        printf("\n");
    }

    return 0;
}