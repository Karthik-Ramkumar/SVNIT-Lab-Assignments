#include <stdio.h>

int main()
{
    int choice;
    int n, i, j, k, t, completed, idx, quantum;
    int pid[50], at[50], bt[50], pr[50];

    printf("CPU Scheduling Simulator\n");
    printf("1. FCFS\n");
    printf("2. SRTF\n");
    printf("3. Priority Scheduling (Non-Preemptive)\n");
    printf("4. Priority Scheduling (Preemptive)\n");
    printf("5. SJF (Non-Preemptive)\n");
    printf("6. Round Robin\n");
    printf("7. Longest Job First (Non-Preemptive)\n");
    printf("8. Longest Remaining Time First\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        printf("\nProcess %d ID: ", i + 1);
        scanf("%d", &pid[i]);

        printf("Arrival Time: ");
        scanf("%d", &at[i]);

        printf("Burst Time: ");
        scanf("%d", &bt[i]);

        if (choice == 3 || choice == 4)
        {
            printf("Priority (smaller number = higher priority): ");
            scanf("%d", &pr[i]);
        }
    }

    if (choice == 1) /* FCFS */
    {
        int temp;
        float avgwt = 0, avgtat = 0;
        int ct[50], tat[50], wt[50];

        for (i = 0; i < n - 1; i++)
        {
            for (j = i + 1; j < n; j++)
            {
                if (at[i] > at[j] || (at[i] == at[j] && pid[i] > pid[j]))
                {
                    temp = at[i]; at[i] = at[j]; at[j] = temp;
                    temp = bt[i]; bt[i] = bt[j]; bt[j] = temp;
                    temp = pid[i]; pid[i] = pid[j]; pid[j] = temp;
                }
            }
        }

        ct[0] = at[0] + bt[0];
        tat[0] = ct[0] - at[0];
        wt[0] = tat[0] - bt[0];

        for (i = 1; i < n; i++)
        {
            if (ct[i - 1] < at[i])
                ct[i] = at[i] + bt[i];
            else
                ct[i] = ct[i - 1] + bt[i];

            tat[i] = ct[i] - at[i];
            wt[i] = tat[i] - bt[i];
        }

        printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 2) /* SRTF */
    {
        int rt[50], ct[50], tat[50], wt[50], done[50];
        float avgwt = 0, avgtat = 0;

        for (i = 0; i < n; i++)
        {
            rt[i] = bt[i];
            done[i] = 0;
        }

        completed = 0;
        t = 0;

        while (completed < n)
        {
            idx = -1;
            int minrt = 999999;

            for (i = 0; i < n; i++)
            {
                if (at[i] <= t && rt[i] > 0)
                {
                    if (rt[i] < minrt)
                    {
                        minrt = rt[i];
                        idx = i;
                    }
                    else if (rt[i] == minrt)
                    {
                        if (at[i] < at[idx])
                            idx = i;
                    }
                }
            }

            if (idx == -1)
            {
                t++;
                continue;
            }

            rt[idx]--;
            t++;

            if (rt[idx] == 0)
            {
                ct[idx] = t;
                tat[idx] = ct[idx] - at[idx];
                wt[idx] = tat[idx] - bt[idx];
                completed++;
            }
        }

        printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 3) /* Priority Non-Preemptive */
    {
        int ct[50], tat[50], wt[50], vis[50];
        float avgwt = 0, avgtat = 0;

        for (i = 0; i < n; i++) vis[i] = 0;

        completed = 0;
        t = 0;

        while (completed < n)
        {
            idx = -1;
            int bestp = 999999;

            for (i = 0; i < n; i++)
            {
                if (!vis[i] && at[i] <= t)
                {
                    if (pr[i] < bestp)
                    {
                        bestp = pr[i];
                        idx = i;
                    }
                    else if (pr[i] == bestp)
                    {
                        if (at[i] < at[idx])
                            idx = i;
                    }
                }
            }

            if (idx == -1)
            {
                t++;
                continue;
            }

            t += bt[idx];
            ct[idx] = t;
            tat[idx] = ct[idx] - at[idx];
            wt[idx] = tat[idx] - bt[idx];
            vis[idx] = 1;
            completed++;
        }

        printf("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], pr[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 4) /* Priority Preemptive */
    {
        int rt[50], ct[50], tat[50], wt[50];
        float avgwt = 0, avgtat = 0;

        for (i = 0; i < n; i++) rt[i] = bt[i];

        completed = 0;
        t = 0;

        while (completed < n)
        {
            idx = -1;
            int bestp = 999999;

            for (i = 0; i < n; i++)
            {
                if (at[i] <= t && rt[i] > 0)
                {
                    if (pr[i] < bestp)
                    {
                        bestp = pr[i];
                        idx = i;
                    }
                    else if (pr[i] == bestp)
                    {
                        if (rt[i] < rt[idx])
                            idx = i;
                    }
                }
            }

            if (idx == -1)
            {
                t++;
                continue;
            }

            rt[idx]--;
            t++;

            if (rt[idx] == 0)
            {
                ct[idx] = t;
                tat[idx] = ct[idx] - at[idx];
                wt[idx] = tat[idx] - bt[idx];
                completed++;
            }
        }

        printf("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], pr[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 5) /* SJF Non-Preemptive */
    {
        int ct[50], tat[50], wt[50], vis[50];
        float avgwt = 0, avgtat = 0;

        for (i = 0; i < n; i++) vis[i] = 0;

        completed = 0;
        t = 0;

        while (completed < n)
        {
            idx = -1;
            int minbt = 999999;

            for (i = 0; i < n; i++)
            {
                if (!vis[i] && at[i] <= t)
                {
                    if (bt[i] < minbt)
                    {
                        minbt = bt[i];
                        idx = i;
                    }
                    else if (bt[i] == minbt)
                    {
                        if (at[i] < at[idx])
                            idx = i;
                    }
                }
            }

            if (idx == -1)
            {
                t++;
                continue;
            }

            t += bt[idx];
            ct[idx] = t;
            tat[idx] = ct[idx] - at[idx];
            wt[idx] = tat[idx] - bt[idx];
            vis[idx] = 1;
            completed++;
        }

        printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 6) /* Round Robin */
    {
        int rt[50], ct[50], tat[50], wt[50], inq[50], q[500];
        int front = 0, rear = 0;
        float avgwt = 0, avgtat = 0;

        printf("Enter Time Quantum: ");
        scanf("%d", &quantum);

        for (i = 0; i < n; i++)
        {
            rt[i] = bt[i];
            inq[i] = 0;
            ct[i] = 0;
        }

        t = 0;
        completed = 0;

        while (completed < n)
        {
            for (i = 0; i < n; i++)
            {
                if (at[i] <= t && rt[i] > 0 && inq[i] == 0)
                {
                    q[rear++] = i;
                    inq[i] = 1;
                }
            }

            if (front == rear)
            {
                t++;
                continue;
            }

            idx = q[front++];
            inq[idx] = 0;

            int run;
            if (rt[idx] < quantum)
                run = rt[idx];
            else
                run = quantum;

            for (k = 0; k < run; k++)
            {
                t++;
                rt[idx]--;

                for (i = 0; i < n; i++)
                {
                    if (at[i] <= t && rt[i] > 0 && inq[i] == 0 && i != idx)
                    {
                        int already = 0;
                        for (j = front; j < rear; j++)
                        {
                            if (q[j] == i)
                            {
                                already = 1;
                                break;
                            }
                        }
                        if (!already)
                        {
                            q[rear++] = i;
                            inq[i] = 1;
                        }
                    }
                }

                if (rt[idx] == 0)
                    break;
            }

            if (rt[idx] > 0)
            {
                q[rear++] = idx;
                inq[idx] = 1;
            }
            else
            {
                ct[idx] = t;
                completed++;
            }
        }

        for (i = 0; i < n; i++)
        {
            tat[i] = ct[i] - at[i];
            wt[i] = tat[i] - bt[i];
        }

        printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 7) /* Longest Job First Non-Preemptive */
    {
        int ct[50], tat[50], wt[50], vis[50];
        float avgwt = 0, avgtat = 0;

        for (i = 0; i < n; i++) vis[i] = 0;

        completed = 0;
        t = 0;

        while (completed < n)
        {
            idx = -1;
            int maxbt = -1;

            for (i = 0; i < n; i++)
            {
                if (!vis[i] && at[i] <= t)
                {
                    if (bt[i] > maxbt)
                    {
                        maxbt = bt[i];
                        idx = i;
                    }
                    else if (bt[i] == maxbt)
                    {
                        if (at[i] < at[idx])
                            idx = i;
                    }
                }
            }

            if (idx == -1)
            {
                t++;
                continue;
            }

            t += bt[idx];
            ct[idx] = t;
            tat[idx] = ct[idx] - at[idx];
            wt[idx] = tat[idx] - bt[idx];
            vis[idx] = 1;
            completed++;
        }

        printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else if (choice == 8) /* LRTF */
    {
        int rt[50], ct[50], tat[50], wt[50];
        float avgwt = 0, avgtat = 0;

        for (i = 0; i < n; i++) rt[i] = bt[i];

        completed = 0;
        t = 0;

        while (completed < n)
        {
            idx = -1;
            int maxrt = -1;

            for (i = 0; i < n; i++)
            {
                if (at[i] <= t && rt[i] > 0)
                {
                    if (rt[i] > maxrt)
                    {
                        maxrt = rt[i];
                        idx = i;
                    }
                    else if (rt[i] == maxrt)
                    {
                        if (at[i] < at[idx])
                            idx = i;
                    }
                }
            }

            if (idx == -1)
            {
                t++;
                continue;
            }

            rt[idx]--;
            t++;

            if (rt[idx] == 0)
            {
                ct[idx] = t;
                tat[idx] = ct[idx] - at[idx];
                wt[idx] = tat[idx] - bt[idx];
                completed++;
            }
        }

        printf("\nPID\tAT\tBT\tCT\tTAT\tWT\n");
        for (i = 0; i < n; i++)
        {
            printf("%d\t%d\t%d\t%d\t%d\t%d\n", pid[i], at[i], bt[i], ct[i], tat[i], wt[i]);
            avgwt += wt[i];
            avgtat += tat[i];
        }

        printf("\nAverage Turnaround Time = %.2f\n", avgtat / n);
        printf("Average Waiting Time    = %.2f\n", avgwt / n);
    }

    else
    {
        printf("Invalid choice.\n");
    }

    return 0;
}