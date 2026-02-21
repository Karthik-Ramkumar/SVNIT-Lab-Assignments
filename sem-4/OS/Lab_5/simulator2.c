#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define MAX 200

typedef struct {
    int pid, at, bt, rt;
    int ct, wt, tat, response;
    int started;
    int priority;
    int deadline;
} Process;

Process original[MAX], p[MAX];
int n;

float avg_w, avg_t, avg_r, cpu_util;

void copy() {
    for(int i=0;i<n;i++)
        p[i]=original[i];
}

void generate_data() {
    srand(time(NULL));
    for(int i=0;i<n;i++) {
        original[i].pid=i+1;
        original[i].at=rand()%10;
        original[i].bt=1+rand()%10;
        original[i].rt=original[i].bt;
        original[i].priority=1+rand()%5;
        original[i].deadline=10+rand()%20;
        original[i].started=0;
    }
}

void write_data_file() {
    FILE *fp=fopen("process_23BCE1234_data.tex","w");
    fprintf(fp,"PID\tAT\tBT\tPR\tDL\n");
    for(int i=0;i<n;i++)
        fprintf(fp,"P%d\t%d\t%d\t%d\t%d\n",
        original[i].pid, original[i].at,
        original[i].bt, original[i].priority,
        original[i].deadline);
    fclose(fp);
}

void calculate_metrics(int total_time) {
    avg_w=avg_t=avg_r=0;
    int busy=0;

    for(int i=0;i<n;i++) {
        p[i].tat=p[i].ct-p[i].at;
        p[i].wt=p[i].tat-p[i].bt;
        avg_w+=p[i].wt;
        avg_t+=p[i].tat;
        avg_r+=p[i].response;
        busy+=p[i].bt;
    }

    avg_w/=n;
    avg_t/=n;
    avg_r/=n;
    cpu_util=(float)busy/total_time*100;
}

void print_results(FILE *fp,char name[]) {

    fprintf(fp,"\n=================================\n");
    fprintf(fp,"Algorithm : %s\n",name);
    fprintf(fp,"=================================\n");

    fprintf(fp,"PID\tWT\tTAT\tRT\n");
    for(int i=0;i<n;i++)
        fprintf(fp,"P%d\t%d\t%d\t%d\n",
        p[i].pid,p[i].wt,p[i].tat,p[i].response);

    fprintf(fp,"\nAverage WT : %.2f\n",avg_w);
    fprintf(fp,"Average TAT : %.2f\n",avg_t);
    fprintf(fp,"Average RT : %.2f\n",avg_r);
    fprintf(fp,"CPU Utilization : %.2f%%\n",cpu_util);
}

/* FCFS */
void FCFS(FILE *fp) {
    copy();
    int time=0;

    for(int i=0;i<n-1;i++)
        for(int j=i+1;j<n;j++)
            if(p[i].at>p[j].at){
                Process t=p[i]; p[i]=p[j]; p[j]=t;
            }

    for(int i=0;i<n;i++) {
        if(time<p[i].at) time=p[i].at;
        p[i].response=time-p[i].at;
        time+=p[i].bt;
        p[i].ct=time;
    }

    calculate_metrics(time);
    print_results(fp,"FCFS");
}

/* SJF */
void SJF(FILE *fp) {
    copy();
    for(int i=0;i<n;i++) p[i].at=0;

    int time=0, done=0;

    while(done<n){
        int idx=-1,min=9999;
        for(int i=0;i<n;i++)
            if(p[i].rt>0 && p[i].bt<min){
                min=p[i].bt;
                idx=i;
            }

        p[idx].response=time;
        time+=p[idx].bt;
        p[idx].rt=0;
        p[idx].ct=time;
        done++;
    }

    calculate_metrics(time);
    print_results(fp,"SJF");
}

/* SRTN */
void SRTN(FILE *fp){
    copy();
    int time=0,done=0;

    while(done<n){
        int idx=-1,min=9999;
        for(int i=0;i<n;i++)
            if(p[i].at<=time && p[i].rt>0 && p[i].rt<min){
                min=p[i].rt; idx=i;
            }

        if(idx==-1){ time++; continue; }

        if(!p[idx].started){
            p[idx].response=time-p[idx].at;
            p[idx].started=1;
        }

        p[idx].rt--; time++;

        if(p[idx].rt==0){
            p[idx].ct=time;
            done++;
        }
    }

    calculate_metrics(time);
    print_results(fp,"SRTN");
}

/* Priority */
void PRIORITY(FILE *fp){
    copy();
    int time=0,done=0;

    while(done<n){
        int idx=-1,high=9999;
        for(int i=0;i<n;i++)
            if(p[i].at<=time && p[i].rt>0 && p[i].priority<high){
                high=p[i].priority; idx=i;
            }

        if(idx==-1){ time++; continue; }

        p[idx].response=time-p[idx].at;
        time+=p[idx].bt;
        p[idx].rt=0;
        p[idx].ct=time;
        done++;
    }

    calculate_metrics(time);
    print_results(fp,"Priority");
}

/* RR */
void RR(FILE *fp,int q){
    copy();
    int time=0,done=0;

    while(done<n){
        int executed=0;

        for(int i=0;i<n;i++){
            if(p[i].at<=time && p[i].rt>0){

                if(!p[i].started){
                    p[i].response=time-p[i].at;
                    p[i].started=1;
                }

                int run=(p[i].rt<q)?p[i].rt:q;
                p[i].rt-=run;
                time+=run;
                executed=1;

                if(p[i].rt==0){
                    p[i].ct=time;
                    done++;
                }
            }
        }
        if(!executed) time++;
    }

    calculate_metrics(time);
    char name[20];
    sprintf(name,"RR (q=%d)",q);
    print_results(fp,name);
}

/* MAIN */
int main(){
    int choice;

    printf("Hi! Welcome to CPU Scheduling Simulator.\n");
    printf("Please give me required parameters.\n\n");

    printf("Scheduling algorithm – (1) FCFS (2) RR (3) SJF (4) SRTN (5) Priority (6) All\n");
    scanf("%d",&choice);

    printf("\nNo. of Processes in the system : ");
    scanf("%d",&n);

    printf("\nWait.... Generating Schedules...\n");

    generate_data();
    write_data_file();

    FILE *fp=fopen("Output.tex","w");

    if(choice==1) FCFS(fp);
    else if(choice==2){ RR(fp,2); RR(fp,4); }
    else if(choice==3) SJF(fp);
    else if(choice==4) SRTN(fp);
    else if(choice==5) PRIORITY(fp);
    else if(choice==6){
        FCFS(fp);
        SJF(fp);
        SRTN(fp);
        PRIORITY(fp);
        RR(fp,2);
        RR(fp,4);
    }

    fclose(fp);

    printf("DONE. Please check output file Output.tex for all the results.\n");

    return 0;
}