#include <stdio.h>

int main() 
{
    char character;

    printf("Enter a character: ");
    scanf("%c", &character);

    // Checking if the character is a capital letter
    if (character >= 'A' && character <= 'Z') 
    {
        printf("'%c' is a capital letter.\n", character);
    }
    // Checking if the character is a small case letter
    else if (character >= 'a' && character <= 'z') 
    {
        printf("'%c' is a small case letter.\n", character);
    }
    // Checking if the character is a digit
    else if (character >= '0' && character <= '9') 
    {
        printf("'%c' is a digit.\n", character);
    }
    // If its not a letter or digit, its a special symbol
    else 
    {
        printf("'%c' is a special symbol.\n", character);
    }

    return 0;
}
