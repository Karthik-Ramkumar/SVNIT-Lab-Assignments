#include <stdio.h>

int graph[50][50];
int visited[50], recStack[50];
int totalNodes;

int hasCycle(int node)
{
    int i;

    visited[node] = 1;
    recStack[node] = 1;

    for (i = 0; i < totalNodes; i++)
    {
        if (graph[node][i] == 1)
        {
            if (!visited[i] && hasCycle(i))
                return 1;
            else if (recStack[i])
                return 1;
        }
    }

    recStack[node] = 0;
    return 0;
}

int main()
{
    int processes, resources;
    int i, j;
    int requestEdges, allocationEdges;
    int p, r;

    printf("Enter number of processes: ");
    scanf("%d", &processes);

    printf("Enter number of resources: ");
    scanf("%d", &resources);

    totalNodes = processes + resources;

    for (i = 0; i < totalNodes; i++)
    {
        for (j = 0; j < totalNodes; j++)
        {
            graph[i][j] = 0;
        }
        visited[i] = 0;
        recStack[i] = 0;
    }

    printf("\nProcess nodes: P0 to P%d\n", processes - 1);
    printf("Resource nodes: R0 to R%d\n", resources - 1);

    printf("\nEnter number of REQUEST edges (Process -> Resource): ");
    scanf("%d", &requestEdges);

    printf("Enter each request edge as: process_index resource_index\n");
    for (i = 0; i < requestEdges; i++)
    {
        scanf("%d %d", &p, &r);
        graph[p][processes + r] = 1;
    }

    printf("\nEnter number of ALLOCATION edges (Resource -> Process): ");
    scanf("%d", &allocationEdges);

    printf("Enter each allocation edge as: resource_index process_index\n");
    for (i = 0; i < allocationEdges; i++)
    {
        scanf("%d %d", &r, &p);
        graph[processes + r][p] = 1;
    }

    printf("\nResource Allocation Graph (Adjacency Matrix):\n");
    printf("    ");
    for (i = 0; i < totalNodes; i++)
    {
        if (i < processes)
            printf("P%d ", i);
        else
            printf("R%d ", i - processes);
    }
    printf("\n");

    for (i = 0; i < totalNodes; i++)
    {
        if (i < processes)
            printf("P%d  ", i);
        else
            printf("R%d  ", i - processes);

        for (j = 0; j < totalNodes; j++)
        {
            printf("%d  ", graph[i][j]);
        }
        printf("\n");
    }

    for (i = 0; i < totalNodes; i++)
    {
        if (!visited[i])
        {
            if (hasCycle(i))
            {
                printf("\nCycle detected in RAG -> Deadlock may exist.\n");
                return 0;
            }
        }
    }

    printf("\nNo cycle detected in RAG -> No deadlock.\n");

    return 0;
}