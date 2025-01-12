#include <stdio.h>
#include <stdlib.h>

int main() {
    int size;

    // Input size of square matrices
    printf("Enter the size of square matrices: ");
    scanf("%d", &size);

    // Allocate memory for the matrices
    int **matrix1 = (int **)malloc(size * sizeof(int *));
    int **matrix2 = (int **)malloc(size * sizeof(int *));
    int **result = (int **)malloc(size * sizeof(int *));
    
    for (int i = 0; i < size; i++) {
        matrix1[i] = (int *)malloc(size * sizeof(int));
        matrix2[i] = (int *)malloc(size * sizeof(int));
        result[i] = (int *)malloc(size * sizeof(int));
    }

    // Input elements for matrix1
    printf("Enter elements for the first matrix:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("Enter element at [%d][%d]: ", i + 1, j + 1);
            scanf("%d", &matrix1[i][j]);
        }
    }

    // Input elements for matrix2
    printf("Enter elements for the second matrix:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("Enter element at [%d][%d]: ", i + 1, j + 1);
            scanf("%d", &matrix2[i][j]);
        }
    }

    // Initialize result matrix to zero
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            result[i][j] = 0;
        }
    }

    // Multiply the matrices
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            for (int k = 0; k < size; k++) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    // Print the result matrix
    printf("\nProduct of the two matrices is:\n");
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%d ", result[i][j]);
        }
        printf("\n");
    }

    // Free allocated memory
    for (int i = 0; i < size; i++) {
        free(matrix1[i]);
        free(matrix2[i]);
        free(result[i]);
    }
    free(matrix1);
    free(matrix2);
    free(result);

    return 0;
}
