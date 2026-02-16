#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>
#include <sched.h>

int global = 100;

int main() {
    int local = 10;
    static int static_var = 50;

    pid_t pid = fork();

    if (pid == 0) {
        printf("Child PID: %d\n", getpid());
        printf("Child Parent PID: %d\n", getppid());

        local++;
        global++;
        static_var++;

        printf("Child -> local=%d global=%d static=%d\n",
               local, global, static_var);

        sleep(2);          // sleep()
        sched_yield();     // yield()

        execl("/bin/ls","ls",NULL);   // exec()

        exit(0);
    }
    else {
        wait(NULL);        // wait()
        printf("Parent PID: %d\n", getpid());
        printf("Parent -> local=%d global=%d static=%d\n",
               local, global, static_var);
	printf("Parent's Parent PID: %d\n", getppid());
    }

    return 0;
}
