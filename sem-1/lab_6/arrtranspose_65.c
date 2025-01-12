#include <stdio.h>

int main() {
    int matrix[3][3], transpose[3][3];

    // Reading the 3x3 matrix
    printf("Enter elements of the 3x3 matrix:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            printf("Element [%d][%d]: ", i+1, j+1);
            scanf("%d", &matrix[i][j]);
        }
    }

    // Calculating transpose
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            transpose[j][i] = matrix[i][j];
        }
    }

    // Printing the transpose
    printf("\nTranspose of the matrix:\n");
    for (int i = 0; i < 3; i++) 
    {
        for (int j = 0; j < 3; j++) 
        {
            printf("%d ", transpose[i][j]);
        }
        printf("\n");
    }

    return 0;
}
