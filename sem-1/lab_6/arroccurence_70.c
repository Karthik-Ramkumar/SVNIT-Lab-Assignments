#include <stdio.h>

int main() {
    int n, element, count = 0;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    int array[n];

    // Reading the array
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < n; i++) {
        printf("Element %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    // Reading the element to check occurrence
    printf("Enter the element to find its occurrence: ");
    scanf("%d", &element);

    // Counting occurrence
    for (int i = 0; i < n; i++) {
        if (array[i] == element) {
            count++;
        }
    }

    printf("The element %d occurs %d time(s) in the array.\n", element, count);

    return 0;
}
