#include <stdio.h>

int main() 
{
    int min, max, check1, input, i;

    printf("Enter how many numbers you want to enter: \n");
    scanf("%d", &input);

    if (input < 1) 
    {
        printf("You need to enter at least 1 number.\n");
        return 0;
    }

    printf("Enter number 1: \n");
    scanf("%d", &max);
    min = max;  // Initialize both min and max with the first input

    for (i = 2; i <= input; i++) 
    {
        printf("Enter number %d: \n", i);
        scanf("%d", &check1);

        if (check1 > max) 
        {
            max = check1;
        }

        if (check1 < min) 
        {
            min = check1;
        }
    }

    printf("Largest number is %d \n", max);
    printf("Smallest number is %d \n", min);

    return 0;
}
