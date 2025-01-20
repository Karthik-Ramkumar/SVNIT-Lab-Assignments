/*WOP to hold two integer pointers as structure members. 
Allocate space for the structure and its data members during runtime. 
Get one array as input. In the second array copy the elements of the first array and replace the odd positioned
elements by the product of its adjacent elements. 
Access the array elements and structures using pointers instead of subscript notation.
First Array (Input)
1 2 3 4 5 6
Second Array (Input)
1 3 3 15 5 6*/
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *arr1;
    int *arr2;
} ArrayStruct;

void processArrays(ArrayStruct *arrays, int size) 
{
    for (int i = 0; i < size; i++) 
    {
        if (i % 2 == 0 || i == 0 || i == size - 1) 
        {
            *(arrays->arr2 + i) = *(arrays->arr1 + i);
        } 
        else 
        {
            *(arrays->arr2 + i) = *(arrays->arr1 + (i - 1)) * *(arrays->arr1 + (i + 1));
        }
    }
}

int main() 
{
    int size;

    printf("Enter the size of the array: ");
    scanf("%d", &size);

    ArrayStruct *arrays = (ArrayStruct *)malloc(sizeof(ArrayStruct));
    arrays->arr1 = (int *)malloc(size * sizeof(int));
    arrays->arr2 = (int *)malloc(size * sizeof(int));

    printf("Enter elements of the array:\n");
    for (int i = 0; i < size; i++) 
    {
        scanf("%d", (arrays->arr1 + i));
    }

    processArrays(arrays, size);

    printf("First Array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", *(arrays->arr1 + i));
    }

    printf("\nSecond Array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", *(arrays->arr2 + i));
    }

    free(arrays->arr1);
    free(arrays->arr2);
    free(arrays);

    return 0;
}
