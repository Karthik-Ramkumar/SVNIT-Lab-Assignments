#include <stdio.h>
#include <stdlib.h>

void read(int **matrix, int size) 
{
    printf("Enter elements of the matrix\n");
    for (int i = 0; i < size; i++) 
    {
        for (int j = 0; j < size; j++) 
        {
            scanf("%d", (*(matrix + i) + j));
        }
    }
}

void multi(int **a, int **b, int **result, int size) 
{
    for (int i = 0; i < size; i++) 
    {
        for (int j = 0; j < size; j++) 
        {
            *(*(result + i) + j) = 0;
            for (int k = 0; k < size; k++) 
            {
                *(*(result + i) + j) += *(*(a + i) + k) * *(*(b + k) + j);
            }
        }
    }
}

void display(int **matrix, int size) 
{
    printf("Matrix:\n", size);
    for (int i = 0; i < size; i++) 
    {
        for (int j = 0; j < size; j++) 
        {
            printf("%d ", *(*(matrix + i) + j));
        }
        printf("\n");
    }
}

int main() 
{
    int size;
    printf("Enter matrix size: \n");
    scanf("%d", &size);

    int **a = (int **)malloc(size * sizeof(int *));
    int **b = (int **)malloc(size * sizeof(int *));
    int **result = (int **)malloc(size * sizeof(int *));

    for (int i = 0; i < size; i++)
        *(a + i) = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++)
        *(b + i) = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++)
        *(result + i) = (int *)malloc(size * sizeof(int));

    read(a, size);
    read(b, size);
    multi(a, b, result, size);

    printf("Resultant Matrix:\n");
    display(result, size);

    for (int i = 0; i < size; i++)
        free(*(a + i));
    for (int i = 0; i < size; i++)
        free(*(b + i));
    for (int i = 0; i < size; i++)
        free(*(result + i));
    free(a);
    free(b);
    free(result);
    return 0;
}
