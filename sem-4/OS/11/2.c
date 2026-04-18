#include <stdio.h>

#define MAX 100

int graph[MAX][MAX];
int visited[MAX];
int recStack[MAX];
int totalNodes;

int dfsCycle(int node)
{
    visited[node] = 1;
    recStack[node] = 1;

    for (int i = 0; i < totalNodes; i++)
    {
        if (graph[node][i] == 1)
        {
            if (visited[i] == 0)
            {
                if (dfsCycle(i))
                    return 1;
            }
            else if (recStack[i] == 1)
            {
                return 1;
            }
        }
    }

    recStack[node] = 0;
    return 0;
}

int detectDeadlock()
{
    for (int i = 0; i < totalNodes; i++)
    {
        visited[i] = 0;
        recStack[i] = 0;
    }

    for (int i = 0; i < totalNodes; i++)
    {
        if (visited[i] == 0)
        {
            if (dfsCycle(i))
                return 1;
        }
    }

    return 0;
}

int main()
{
    int processes, resources;
    int edges;
    int from, to;

    printf("Enter number of processes: ");
    scanf("%d", &processes);

    printf("Enter number of resources: ");
    scanf("%d", &resources);

    totalNodes = processes + resources;

    for (int i = 0; i < totalNodes; i++)
    {
        for (int j = 0; j < totalNodes; j++)
        {
            graph[i][j] = 0;
        }
    }

    printf("\nNode numbering:\n");
    printf("Processes: 0 to %d\n", processes - 1);
    printf("Resources: %d to %d\n", processes, totalNodes - 1);

    printf("\nEnter number of edges in RAG: ");
    scanf("%d", &edges);

    printf("Enter edges (from to):\n");
    printf("For request edge: Process -> Resource\n");
    printf("For allocation edge: Resource -> Process\n\n");

    for (int i = 0; i < edges; i++)
    {
        scanf("%d %d", &from, &to);
        graph[from][to] = 1;
    }

    printf("\nResource Allocation Graph Adjacency Matrix:\n");
    for (int i = 0; i < totalNodes; i++)
    {
        for (int j = 0; j < totalNodes; j++)
        {
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }

    if (detectDeadlock())
        printf("\nCycle detected in RAG -> Deadlock may exist.\n");
    else
        printf("\nNo cycle detected in RAG -> No deadlock.\n");

    return 0;
}