#include <stdio.h>

int n, m;
int allocation[10][10], max[10][10], need[10][10];
int available[10];
int dataEntered = 0;

void calculateNeed()
{
    int i, j;
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }
}

int checkSafeState()
{
    int work[10], finish[10] = {0}, safeSequence[10];
    int i, j, k, count = 0, found;

    for(i = 0; i < m; i++)
    {
        work[i] = available[i];
    }

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
        printf("\nSystem is in SAFE state.\n");
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
        return 1;
    }
    else
    {
        printf("\nSystem is in UNSAFE state.\n");
        return 0;
    }
}

void enterData()
{
    int i, j;

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

    calculateNeed();
    dataEntered = 1;
    printf("\nData entered successfully.\n");
}

void displayNeed()
{
    int i, j;

    if(dataEntered == 0)
    {
        printf("\nPlease enter data first.\n");
        return;
    }

    printf("\nNEED MATRIX:\n");
    printf("     ");
    for(j = 0; j < m; j++)
    {
        printf("R%d ", j);
    }
    printf("\n");

    for(i = 0; i < n; i++)
    {
        printf("P%d   ", i);
        for(j = 0; j < m; j++)
        {
            printf("%d  ", need[i][j]);
        }
        printf("\n");
    }
}

void processRequest()
{
    int process, request[10];
    int i;
    int tempAvailable[10], tempAllocation[10][10], tempNeed[10][10];

    if(dataEntered == 0)
    {
        printf("\nPlease enter data first.\n");
        return;
    }

    printf("Enter process number (0 to %d): ", n - 1);
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
            return;
        }
    }

    for(i = 0; i < m; i++)
    {
        if(request[i] > available[i])
        {
            printf("\nRequest cannot be granted (Request > Available)\n");
            return;
        }
    }

    for(i = 0; i < m; i++)
    {
        tempAvailable[i] = available[i];
    }

    for(i = 0; i < n; i++)
    {
        int j;
        for(j = 0; j < m; j++)
        {
            tempAllocation[i][j] = allocation[i][j];
            tempNeed[i][j] = need[i][j];
        }
    }

    for(i = 0; i < m; i++)
    {
        available[i] = available[i] - request[i];
        allocation[process][i] = allocation[process][i] + request[i];
        need[process][i] = need[process][i] - request[i];
    }

    if(checkSafeState())
    {
        printf("Request GRANTED.\n");
    }
    else
    {
        for(i = 0; i < m; i++)
        {
            available[i] = tempAvailable[i];
        }

        for(i = 0; i < n; i++)
        {
            int j;
            for(j = 0; j < m; j++)
            {
                allocation[i][j] = tempAllocation[i][j];
                need[i][j] = tempNeed[i][j];
            }
        }

        printf("Request DENIED.\n");
    }
}

int main()
{
    int choice;

    while(1)
    {
        printf("\n--- BANKER'S ALGORITHM MENU ---\n");
        printf("1. Enter data\n");
        printf("2. Display Need matrix\n");
        printf("3. Check safe state\n");
        printf("4. Process resource request\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                enterData();
                break;

            case 2:
                displayNeed();
                break;

            case 3:
                if(dataEntered == 0)
                {
                    printf("\nPlease enter data first.\n");
                }
                else
                {
                    checkSafeState();
                }
                break;

            case 4:
                processRequest();
                break;

            case 5:
                return 0;

            default:
                printf("\nInvalid choice.\n");
        }
    }

    return 0;
}