#include <stdio.h>
#include <pthread.h>

int arr[100], n;
int maximum, minimum;

void *find_max(void *arg)
{
    int i;
    maximum = arr[0];

    for(i = 1; i < n; i++)
    {
        if(arr[i] > maximum)
        {
            maximum = arr[i];
        }
    }
    return NULL;
}

void *find_min(void *arg)
{
    int i;
    minimum = arr[0];

    for(i = 1; i < n; i++)
    {
        if(arr[i] < minimum)
        {
            minimum = arr[i];
        }
    }
    return NULL;
}

int main()
{
    pthread_t t1, t2;
    int i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter array elements: ");
    for(i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    pthread_create(&t1, NULL, find_max, NULL);
    pthread_create(&t2, NULL, find_min, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Maximum = %d\n", maximum);
    printf("Minimum = %d\n", minimum);

    return 0;
}