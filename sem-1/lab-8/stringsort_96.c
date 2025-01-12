#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Function to swap two strings using pointers
void swap(char **str1, char **str2) 
{
    char *temp = *str1;
    *str1 = *str2;
    *str2 = temp;
}

int main() 
{
    int n;
    printf("Enter the number of strings: ");
    scanf("%d", &n);
    char *arr[n];
    getchar();  // To consume the newline character left by previous scanf
    for (int i = 0; i < n; i++) 
    {
        arr[i] = (char *)malloc(100 * sizeof(char));  // Allocate memory for each string
        printf("Enter string %d: ", i + 1);
        gets(arr[i]);  // Use gets() to read the string
    }

    // Sort strings in ascending order using pointer comparisons
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (strcmp(arr[i], arr[j]) > 0) {
                swap(&arr[i], &arr[j]);  // Swap pointers
            }
        }
    }

    // Print the sorted strings
    printf("\nSorted strings in ascending order:\n");
    for (int i = 0; i < n; i++) {
        printf("%s\n", arr[i]);
    }

    // Free allocated memory
    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }

    return 0;
}
