#include <stdio.h>
#include <pthread.h>

void *child_thread(void *arg)
{
    printf("Hello from child thread\n");
    return NULL;
}

int main()
{
    pthread_t thread;

    printf("Hello from main thread\n");

    pthread_create(&thread, NULL, child_thread, NULL);

    pthread_join(thread, NULL);

    printf("Main thread finished\n");

    return 0;
}