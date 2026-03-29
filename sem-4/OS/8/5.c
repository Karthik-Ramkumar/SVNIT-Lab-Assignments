#include <stdio.h>
#include <pthread.h>

int n;
long long factorial = 1;
int sum = 0;

void *find_factorial(void *arg)
{
    int i;
    for(i = 1; i <= n; i++)
    {
        factorial = factorial * i;
    }
    return NULL;
}

void *find_sum(void *arg)
{
    int i;
    for(i = 1; i <= n; i++)
    {
        sum = sum + i;
    }
    return NULL;
}

int main()
{
    pthread_t t1, t2;

    printf("Enter value of N: ");
    scanf("%d", &n);

    pthread_create(&t1, NULL, find_factorial, NULL);
    pthread_create(&t2, NULL, find_sum, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Factorial of %d = %lld\n", n, factorial);
    printf("Sum of first %d natural numbers = %d\n", n, sum);

    return 0;
}