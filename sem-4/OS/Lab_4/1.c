#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        printf("Child process\n");
        execl("/bin/ls", "ls", NULL);   // exec()
        exit(0);                        // exit()
    } else {
        wait(NULL);                     // wait()
        printf("Parent process\n");
    }

    return 0;
}
