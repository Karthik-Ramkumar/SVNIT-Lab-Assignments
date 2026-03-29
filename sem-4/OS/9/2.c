#include <stdio.h>

int main()
{
    int n, m;
    int allocation[10][10], max[10][10], need[10][10];
    int available[10], work[10];
    int finish[10], safeSequence[10];
    int request[10];
    int i, j, k, count, found;
    int process;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    printf("Enter number of resources: ");
    scanf("%d", &m);

    printf("Enter Allocation Matrix:\n");
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
        {
            scanf("%d", &allocation[i][j]);
        }
    }

    printf("Enter Max Matrix:\n");
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
        {
            scanf("%d", &max[i][j]);
        }
    }

    printf("Enter Available Resources:\n");
    for(i = 0; i < m; i++)
    {
        scanf("%d", &available[i]);
    }

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    printf("\nNeed Matrix:\n");
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
        {
            printf("%d ", need[i][j]);
        }
        printf("\n");
    }

    printf("\nEnter process number for request (0 to %d): ", n - 1);
    scanf("%d", &process);

    printf("Enter request vector:\n");
    for(i = 0; i < m; i++)
    {
        scanf("%d", &request[i]);
    }

    for(i = 0; i < m; i++)
    {
        if(request[i] > need[process][i])
        {
            printf("\nRequest cannot be granted (Request > Need)\n");
            return 0;
        }
    }

    for(i = 0; i < m; i++)
    {
        if(request[i] > available[i])
        {
            printf("\nRequest cannot be granted (Request > Available)\n");
            return 0;
        }
    }

    for(i = 0; i < m; i++)
    {
        available[i] = available[i] - request[i];
        allocation[process][i] = allocation[process][i] + request[i];
        need[process][i] = need[process][i] - request[i];
    }

    for(i = 0; i < m; i++)
    {
        work[i] = available[i];
    }

    for(i = 0; i < n; i++)
    {
        finish[i] = 0;
    }

    count = 0;

    while(count < n)
    {
        found = 0;

        for(i = 0; i < n; i++)
        {
            if(finish[i] == 0)
            {
                int possible = 1;

                for(j = 0; j < m; j++)
                {
                    if(need[i][j] > work[j])
                    {
                        possible = 0;
                        break;
                    }
                }

                if(possible == 1)
                {
                    for(k = 0; k < m; k++)
                    {
                        work[k] = work[k] + allocation[i][k];
                    }

                    safeSequence[count] = i;
                    finish[i] = 1;
                    count++;
                    found = 1;
                }
            }
        }

        if(found == 0)
        {
            break;
        }
    }

    if(count == n)
    {
        printf("\nRequest can be GRANTED.\n");
        printf("System remains in SAFE state.\n");
        printf("Safe Sequence: ");
        for(i = 0; i < n; i++)
        {
            printf("P%d", safeSequence[i]);
            if(i != n - 1)
            {
                printf(" -> ");
            }
        }
        printf("\n");
    }
    else
    {
        printf("\nRequest cannot be GRANTED.\n");
        printf("System will be in UNSAFE state.\n");
    }

    return 0;
}