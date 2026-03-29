#include <stdio.h>

int main()
{
    int n, m;
    int allocation[10][10], max[10][10], need[10][10], available[10];
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

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < m; j++)
        {
            need[i][j] = max[i][j] - allocation[i][j];
        }
    }

    printf("\nALLOCATION MATRIX:\n");
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
            printf("%d  ", allocation[i][j]);
        }
        printf("\n");
    }

    printf("\nMAX MATRIX:\n");
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
            printf("%d  ", max[i][j]);
        }
        printf("\n");
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

    printf("\nAVAILABLE MATRIX:\n");
    printf("     ");
    for(j = 0; j < m; j++)
    {
        printf("R%d ", j);
    }
    printf("\n     ");

    for(j = 0; j < m; j++)
    {
        printf("%d  ", available[j]);
    }
    printf("\n");

    return 0;
}