#include <stdio.h>

int main() 
{
    char character;
    int ascii;
    
    printf("Enter a character: ");
    scanf("%c", &character);

    // Converting the character to its ASCII value
    ascii = (int) character;

    // Displaying the ASCII value
    printf("The ASCII value of '%c' is %d\n", character, ascii);

    return 0;
}
