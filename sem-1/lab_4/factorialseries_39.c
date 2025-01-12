#include <stdio.h>

int main() 
{
    int input;
    float factorial, total = 0;

    printf("Enter how long the series should be: \n");
    scanf("%d", &input);

    for (int i = 1; i <= input; i++) 
    {
        factorial = 1;  // Reset factorial for each i

        for (int j = 1; j <= i; j++) 
        {
            factorial *= j;
        }

        float term = (float)i / factorial;
        total += term;  // Add the term to the total sum

        if (i == 1) 
        {
            printf("%f", term);
        } 
        else 
        {
            printf(" + %f", term);
        }
    }

    printf("\nSum of the series: %f\n", total);
    return 0;
}
