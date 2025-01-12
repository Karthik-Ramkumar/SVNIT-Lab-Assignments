#include <stdio.h>

int main() 
{
    char ch;

    printf("Enter a character: ");
    scanf(" %c", &ch);

    printf("%c is %s\n", ch, (ch >= 'a' && ch <= 'z') ? "a small case letter" : "not a small case letter");

    return 0;
}