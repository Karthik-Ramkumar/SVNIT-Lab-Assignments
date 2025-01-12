#include <stdio.h>

int main() 
{
    int n, num, max, second_max;

    printf("How many numbers do you want to input? ");
    scanf("%d", &n);

    if (n < 2) 
    {
        printf("You need to enter at least 2 numbers.\n");
        return 0;
    }

    printf("Enter number 1: ");
    scanf("%d", &max);

    //second_max = -2147483648;  // Initialize second max to the smallest possible int

    for (int i = 2; i <= n; i++) 
    {
        printf("Enter number %d: ", i);
        scanf("%d", &num);

        if (num > max) 
        {
            second_max = max;
            max = num;
        } 
        else if (num > second_max) 
        {
            second_max = num;
        }
    }

    printf("Maximum: %d\n", max);
    printf("Second Maximum: %d\n", second_max);

    return 0;
}
