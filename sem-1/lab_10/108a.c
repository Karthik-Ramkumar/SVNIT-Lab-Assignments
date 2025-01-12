#include <stdio.h>

void copyString(char *source, char *destination) 
{
    while (*source) {
        *destination = *source;
        source++;
        destination++;
    }
    *destination = '\0';
}

int main() 
{
    char source[] = "Hello, World!";
    char destination[100];

    copyString(source, destination);
    printf("Copied string: %s\n", destination);

    return 0;
}