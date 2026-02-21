#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX 100

typedef struct {
    int pid;
    int arrival;
    int burst;
    int remaining;
    int completion;
    int waiting;
    int turnaround;
    int response;
    int started;
    int priority;
    int deadline;
} Process;

Process original[MAX];
Process proc[MAX];

int n;

/* ---------- Utility ---------- */

void copy_processes() {
    for(int i=0;i<n;i++)
        proc[i] = original[i];
}

void generate_processes() {
    srand(time(NULL));

    for(int i=0;i<n;i++) {
        original[i].pid = i+1;
        original[i].arrival = rand()%10;
        original[i].burst = 1 + rand()%10;
        original[i].remaining = original[i].burst;
        original[i].priority = 1 + rand()%5;
        original[i].deadline = 10 + rand()%20;
        original[i].started = 0;
    }
}

void print_input() {
    printf("\nPID\tAT\tBT\tPR\tDL\n");
    for(int i=0;i<n;i++)
        printf("P%d\t%d\t%d\t%d\t%d\n",
        original[i].pid,
        original[i].arrival,
        original[i].burst,
        original[i].priority,
        original[i].deadline);
}

/* ---------- Metrics ---------- */

void calculate_metrics(int total_time) {
    float avg_w=0, avg_t=0, avg_r=0;

    printf("\nPID\tWT\tTAT\tRT\n");
    for(int i=0;i<n;i++) {
        proc[i].turnaround = proc[i].completion - proc[i].arrival;
        proc[i].waiting = proc[i].turnaround - proc[i].burst;

        avg_w += proc[i].waiting;
        avg_t += proc[i].turnaround;
        avg_r += proc[i].response;

        printf("P%d\t%d\t%d\t%d\n",
        proc[i].pid,
        proc[i].waiting,
        proc[i].turnaround,
        proc[i].response);
    }

    printf("\nAverage Waiting Time = %.2f", avg_w/n);
    printf("\nAverage Turnaround Time = %.2f", avg_t/n);
    printf("\nAverage Response Time = %.2f", avg_r/n);

    int busy=0;
    for(int i=0;i<n;i++)
        busy += proc[i].burst;

    printf("\nCPU Utilization = %.2f%%\n",
           (float)busy/total_time*100);
}

/* ---------- FCFS ---------- */

void FCFS() {
    copy_processes();

    int time=0;

    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
            if(proc[i].arrival > proc[j].arrival) {
                Process t=proc[i]; proc[i]=proc[j]; proc[j]=t;
            }

    for(int i=0;i<n;i++) {
        if(time < proc[i].arrival)
            time = proc[i].arrival;

        proc[i].response = time - proc[i].arrival;
        time += proc[i].burst;
        proc[i].completion = time;
    }

    printf("\n===== FCFS =====\n");
    calculate_metrics(time);
}

/* ---------- SJF (Non Preemptive) ---------- */

void SJF() {
    copy_processes();

    for(int i=0;i<n;i++)
        proc[i].arrival = 0;

    int time=0, done=0;

    printf("\n===== SJF (Non Preemptive) =====\n");

    while(done<n) {
        int idx=-1, min=9999;

        for(int i=0;i<n;i++) {
            if(proc[i].remaining>0 && proc[i].burst<min) {
                min = proc[i].burst;
                idx = i;
            }
        }

        proc[idx].response = time;
        time += proc[idx].burst;
        proc[idx].remaining=0;
        proc[idx].completion = time;
        done++;
    }

    calculate_metrics(time);
}

/* ---------- SRTN ---------- */

void SRTN() {
    copy_processes();

    int time=0, done=0;

    printf("\n===== SRTN (Preemptive SJF) =====\n");

    while(done<n) {
        int idx=-1, min=9999;

        for(int i=0;i<n;i++) {
            if(proc[i].arrival<=time && proc[i].remaining>0 &&
               proc[i].remaining<min) {
                min=proc[i].remaining;
                idx=i;
            }
        }

        if(idx==-1) { time++; continue; }

        if(!proc[idx].started) {
            proc[idx].response = time - proc[idx].arrival;
            proc[idx].started=1;
        }

        proc[idx].remaining--;
        time++;

        if(proc[idx].remaining==0) {
            proc[idx].completion=time;
            done++;
        }
    }

    calculate_metrics(time);
}

/* ---------- Priority (Non Preemptive) ---------- */

void PRIORITY() {
    copy_processes();

    int time=0, done=0;

    printf("\n===== Priority (Non Preemptive) =====\n");

    while(done<n) {
        int idx=-1, high=9999;

        for(int i=0;i<n;i++) {
            if(proc[i].arrival<=time && proc[i].remaining>0 &&
               proc[i].priority<high) {
                high=proc[i].priority;
                idx=i;
            }
        }

        if(idx==-1) { time++; continue; }

        proc[idx].response = time - proc[idx].arrival;
        time += proc[idx].burst;
        proc[idx].remaining=0;
        proc[idx].completion=time;
        done++;
    }

    calculate_metrics(time);
}

/* ---------- Round Robin ---------- */

void RR(int quantum) {
    copy_processes();

    int time=0, done=0;

    printf("\n===== Round Robin (q=%d) =====\n", quantum);

    while(done<n) {
        int executed=0;

        for(int i=0;i<n;i++) {
            if(proc[i].arrival<=time && proc[i].remaining>0) {

                if(!proc[i].started) {
                    proc[i].response=time-proc[i].arrival;
                    proc[i].started=1;
                }

                int run = (proc[i].remaining<quantum) ?
                           proc[i].remaining : quantum;

                proc[i].remaining -= run;
                time += run;
                executed=1;

                if(proc[i].remaining==0) {
                    proc[i].completion=time;
                    done++;
                }
            }
        }

        if(!executed) time++;
    }

    calculate_metrics(time);
}

/* ---------- MAIN ---------- */

int main(int argc, char *argv[]) {

    if(argc!=3) {
        printf("Usage: ./simulator <ALGO/ALL> <No_of_Processes>\n");
        return 0;
    }

    n = atoi(argv[2]);

    generate_processes();
    print_input();

    if(strcmp(argv[1],"FCFS")==0)
        FCFS();
    else if(strcmp(argv[1],"SJF")==0)
        SJF();
    else if(strcmp(argv[1],"SRTN")==0)
        SRTN();
    else if(strcmp(argv[1],"PRIORITY")==0)
        PRIORITY();
    else if(strcmp(argv[1],"RR")==0) {
        RR(2);
        RR(4);
    }
    else if(strcmp(argv[1],"ALL")==0) {
        FCFS();
        SJF();
        SRTN();
        PRIORITY();
        RR(2);
        RR(4);
    }
    else
        printf("Invalid Algorithm\n");

    return 0;
}