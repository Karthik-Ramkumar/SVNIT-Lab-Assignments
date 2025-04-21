// first make an array of size of highest element.
// then store the occurence number of each element in the array.
// then sort the array and then print the elements and their occurence number.
#include <stdio.h>
#define MAX 100

void countingSort(int arr[], int n)
{
    int output[n];
    int count[MAX] = {0};

    for (int i = 0; i < n; i++)
        count[arr[i]]++;

    int k = 0;
    for (int i = 0; i < MAX; i++)
    {
        while (count[i] > 0)
        {
            output[k++] = i;
            count[i]--;
        }
    }

    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

int main()
{
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = 7;

    countingSort(arr, n);

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}

