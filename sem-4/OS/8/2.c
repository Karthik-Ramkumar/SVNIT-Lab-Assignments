#include <stdio.h>
#include <pthread.h>

void *print_even(void *arg)
{
    int i;
    for(i = 1; i <= 20; i++)
    {
        if(i % 2 == 0)
        {
            printf("Even: %d\n", i);
        }
    }
    return NULL;
}

void *print_odd(void *arg)
{
    int i;
    for(i = 1; i <= 20; i++)
    {
        if(i % 2 != 0)
        {
            printf("Odd: %d\n", i);
        }
    }
    return NULL;
}

int main()
{
    pthread_t t1, t2;

    pthread_create(&t1, NULL, print_even, NULL);
    pthread_create(&t2, NULL, print_odd, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    return 0;
}