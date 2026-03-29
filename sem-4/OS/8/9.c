#include <stdio.h>
#include <pthread.h>

int a[10][10], b[10][10], result[10][10];
int r1, c1, r2, c2;

void *matrix_addition(void *arg)
{
    int i, j;
    for(i = 0; i < r1; i++)
    {
        for(j = 0; j < c1; j++)
        {
            result[i][j] = a[i][j] + b[i][j];
        }
    }
    return NULL;
}

int main()
{
    pthread_t t1;
    int i, j;

    printf("Enter rows and columns of first matrix: ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and columns of second matrix: ");
    scanf("%d %d", &r2, &c2);

    if(r1 != r2 || c1 != c2)
    {
        printf("Matrix addition not possible\n");
        return 0;
    }

    printf("Enter elements of first matrix:\n");
    for(i = 0; i < r1; i++)
    {
        for(j = 0; j < c1; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }

    printf("Enter elements of second matrix:\n");
    for(i = 0; i < r2; i++)
    {
        for(j = 0; j < c2; j++)
        {
            scanf("%d", &b[i][j]);
        }
    }

    pthread_create(&t1, NULL, matrix_addition, NULL);
    pthread_join(t1, NULL);

    printf("Resultant matrix after addition:\n");
    for(i = 0; i < r1; i++)
    {
        for(j = 0; j < c1; j++)
        {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    return 0;
}