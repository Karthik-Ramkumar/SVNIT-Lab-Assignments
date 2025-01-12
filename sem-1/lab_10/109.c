#include <stdio.h>

// Function to reverse a string
void reverseString(char *str) {
    char *start = str;
    char *end = str;
    char temp;

    while (*end) {
        end++;
    }
    end--;

    while (start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

int main() {
    char str[] = "Hello, World!";

    // Call the function to reverse the string
    reverseString(str);

    // Print the reversed string
    printf("Reversed string: %s\n", str);

    return 0;
}