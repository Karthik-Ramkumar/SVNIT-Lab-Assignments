#include <stdio.h>

int main() 
{
    int n, max, secondMax;
    
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    if (n < 2) 
    {
        printf("Need at least two numbers.\n");
        return 1;
    }

    int numbers[n];

    // Reading numbers
    for (int i = 0; i < n; i++) 
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", &numbers[i]);
    }

    // Initialize max and secondMax
    if (numbers[0] > numbers[1]) 
    {
        max = numbers[0];
        secondMax = numbers[1];
    } else {
        max = numbers[1];
        secondMax = numbers[0];
    }

    // Find max and second max
    for (int i = 2; i < n; i++) 
    {
        if (numbers[i] > max) 
        {
            secondMax = max;
            max = numbers[i];
        } else if (numbers[i] > secondMax && numbers[i] != max) 
        {
            secondMax = numbers[i];
        }
    }

    printf("Maximum: %d\n", max);
    printf("Second Maximum: %d\n", secondMax);

    return 0;
}
