#include <stdio.h>

void merge(int arr[], int l, int m, int r) {
    int i = l, j = m + 1, k = 0;
    int temp[r - l + 1];

    while (i <= m && j <= r) {
        if (arr[i] <= arr[j]) 
            temp[k++] = arr[i++];
        else 
            temp[k++] = arr[j++];
    }

    while (i <= m) 
        temp[k++] = arr[i++];
    
    while (j <= r) 
        temp[k++] = arr[j++];

    for (i = l, k = 0; i <= r; i++, k++) 
        arr[i] = temp[k];
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

int main() {
    int arr[] = {4, 1, 3, 9, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++) 
        printf("%d ", arr[i]);
    
    return 0;
}
