#include <stdio.h>

int main()
 {
    int num, sum = 0;

    // Reading numbers until a negative number is entered
    while (1) 
    {
        printf("Enter a number (negative number to stop): ");
        scanf("%d", &num);

        if (num < 0)
         {
            break;
        }

        sum += num;
    }

    printf("Sum of the numbers: %d\n", sum);
    return 0;
}
