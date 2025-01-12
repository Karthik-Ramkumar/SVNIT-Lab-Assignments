/*#include <stdio.h>

int main() 
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num <= 1) 
    {
        printf("%d is not a prime number.\n", num);
    } 
    else 
    {
        int is_prime = 1;
        for (int i = 2; i * i <= num; i++) 
        {
            if (num % i == 0) 
            {
                is_prime = 0;
                break;
            }
        }
        if (is_prime) 
        {
            printf("%d is a prime number.\n", num);
        } 
        else 
        {
            printf("%d is not a prime number.\n", num);
        }
    }

    return 0;
}*/

#include <stdio.h>

int main() 
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (num <= 1) 
    {
        printf("%d is not a prime number.\n", num);
    } 
    //------------------------------------------
    else 
    {
        int i = 2;
        int isprime = 0;
        while (i < num) 
        {
            if (num % i == 0) 
            {   
                isprime = 1;
                break;
            }
            i++;
        }
        if (isprime == 0) 
        {
            printf("%d is a prime number.\n", num);
        } 
        else
        {
            printf("%d is not a prime number.\n", num);
        }
    }

    return 0;
}
