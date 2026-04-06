#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5

sem_t chopstick[N];

void *philosopher(void *arg)
{
    int philosopher_number = *(int *)arg;
    int left = philosopher_number;
    int right = (philosopher_number + 1) % N;
    int i;

    for (i = 0; i < 3; i++)
    {
        printf("Philosopher %d is thinking\n", philosopher_number);
        sleep(1);

        if (philosopher_number == N - 1)
        {
            sem_wait(&chopstick[right]);
            sem_wait(&chopstick[left]);
        }
        else
        {
            sem_wait(&chopstick[left]);
            sem_wait(&chopstick[right]);
        }

        printf("Philosopher %d is eating\n", philosopher_number);
        sleep(1);

        sem_post(&chopstick[left]);
        sem_post(&chopstick[right]);
    }

    pthread_exit(NULL);
}

int main()
{
    pthread_t philosopher_threads[N];
    int philosopher_numbers[N];
    int i;

    for (i = 0; i < N; i++)
    {
        sem_init(&chopstick[i], 0, 1);
    }

    for (i = 0; i < N; i++)
    {
        philosopher_numbers[i] = i;
        pthread_create(&philosopher_threads[i], NULL, philosopher, &philosopher_numbers[i]);
    }

    for (i = 0; i < N; i++)
    {
        pthread_join(philosopher_threads[i], NULL);
    }

    for (i = 0; i < N; i++)
    {
        sem_destroy(&chopstick[i]);
    }

    return 0;
}