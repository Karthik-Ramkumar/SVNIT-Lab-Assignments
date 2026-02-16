#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main(int argc, char *argv[]) {

    if (argc != 2) {
        printf("Usage: %s <positive_integer>\n", argv[0]);
        return 1;
    }

    int number = atoi(argv[1]);

    if (number <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    pid_t pid = fork();

    if (pid < 0) {
        printf("Fork failed.\n");
        return 1;
    }
    else if (pid == 0) {
        // Child process
        printf("Sequence: ");
        while (number >= 1) {
            printf("%d ", number);
            number = number / 2;
        }
        printf("\n");
        exit(0);
    }
    else {
        // Parent process
        wait(NULL);
        printf("Child process completed.\n");
    }

    return 0;
}
