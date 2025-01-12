#include <stdio.h>

int main()
 {
    int n, i, isPrime = 1;

    printf("Enter a number: ");
    scanf("%d", &n);

    if (n <= 1) 
    {
        printf("%d is neither prime nor composite.\n", n);
    }
     lse 
    {
        for (i = 2; i <= n / 2; i++)
        {
            if (n % i == 0)
            {
                isPrime = 0; // Not prime
                break;
            }
        }

        if (isPrime) 
        {
            printf("%d is a prime number.\n", n);
        }
         else
        {
            printf("%d is a composite number.\n", n);
        }
    }

    return 0;
}
