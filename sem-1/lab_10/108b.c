#include <stdio.h>

// Function to compare two strings
int compareStrings(char *str1, char *str2) {
    while (*str1 && (*str1 == *str2)) {
        str1++;
        str2++;
    }
    return *(unsigned char *)str1 - *(unsigned char *)str2;
}

int main() {
    char str1[] = "Hello";
    char str2[] = "World";

    // Call the function to compare the strings
    int result = compareStrings(str1, str2);

    // Print the comparison result
    if (result < 0) {
        printf("String 1 is less than String 2\n");
    } else if (result > 0) {
        printf("String 1 is greater than String 2\n");
    } else {
        printf("String 1 is equal to String 2\n");
    }

    return 0;
}