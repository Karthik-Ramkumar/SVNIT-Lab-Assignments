#include <stdio.h>

void merge_sort(int arr[], int start, int end);
void merge(int arr[], int start, int mid, int end);

void merge_sort(int arr[], int start, int end)
{
    if(start < end)
    {
        int mid = start + (end - start) / 2; // or (mid = (start + end) / 2)
        merge_sort(arr, start, mid);
        merge_sort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

void merge(int arr[], int start, int mid, int end)
{
    int i = start, j = mid + 1, k = 0;
    int temp[end - start + 1];

    while(i <= mid && j <= end)
    {
        if(arr[i] < arr[j]) // change it to >= to descending order
            temp[k++] = arr[i++];
        else
            temp[k++] = arr[j++];
    }

    while(i <= mid)
        temp[k++] = arr[i++];
    
    while(j <= end)
        temp[k++] = arr[j++];

    for(i = start, k = 0; i <= end; i++, k++)
        arr[i] = temp[k];
}
int main() {
    int arr[] = {38, 27, 43, 3, 9, 82, 10, 45, 12, 6};
    int n = 10; // size of the array
    merge_sort(arr, 0, n - 1);
    for(int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
// Time Complexity: O(n log n)
// Space Complexity: O(n)