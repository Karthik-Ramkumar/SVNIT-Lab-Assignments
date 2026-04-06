#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

int read_count = 0;
int shared_data = 0;

sem_t mutex, write_lock;

void *reader(void *arg)
{
    int reader_number = *(int *)arg;
    int i;

    for (i = 0; i < 3; i++)
    {
        sem_wait(&mutex);
        read_count++;

        if (read_count == 1)
        {
            sem_wait(&write_lock);
        }

        sem_post(&mutex);

        printf("Reader %d is reading shared data = %d\n", reader_number, shared_data);
        sleep(1);

        sem_wait(&mutex);
        read_count--;

        if (read_count == 0)
        {
            sem_post(&write_lock);
        }

        sem_post(&mutex);

        sleep(1);
    }

    pthread_exit(NULL);
}

void *writer(void *arg)
{
    int writer_number = *(int *)arg;
    int i;

    for (i = 0; i < 3; i++)
    {
        sem_wait(&write_lock);

        shared_data++;
        printf("Writer %d is writing shared data = %d\n", writer_number, shared_data);
        sleep(1);

        sem_post(&write_lock);

        sleep(1);
    }

    pthread_exit(NULL);
}

int main()
{
    pthread_t reader_threads[3], writer_threads[2];
    int reader_numbers[3], writer_numbers[2];
    int i;

    sem_init(&mutex, 0, 1);
    sem_init(&write_lock, 0, 1);

    for (i = 0; i < 3; i++)
    {
        reader_numbers[i] = i + 1;
        pthread_create(&reader_threads[i], NULL, reader, &reader_numbers[i]);
    }

    for (i = 0; i < 2; i++)
    {
        writer_numbers[i] = i + 1;
        pthread_create(&writer_threads[i], NULL, writer, &writer_numbers[i]);
    }

    for (i = 0; i < 3; i++)
    {
        pthread_join(reader_threads[i], NULL);
    }

    for (i = 0; i < 2; i++)
    {
        pthread_join(writer_threads[i], NULL);
    }

    sem_destroy(&mutex);
    sem_destroy(&write_lock);

    return 0;
}