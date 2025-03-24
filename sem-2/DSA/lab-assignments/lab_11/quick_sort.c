#include <stdio.h>

int partition(int arr[], int left, int right) {
    int pivot = arr[right];
    int i = left - 1, temp;

    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            i++;
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    temp = arr[i + 1];
    arr[i + 1] = arr[right];
    arr[right] = temp;

    return i + 1;
}

int quickSelect(int arr[], int left, int right, int k) {
    if (left <= right) {
        int pivotIndex = partition(arr, left, right);

        if (pivotIndex == k)
            return arr[pivotIndex];
        else if (pivotIndex > k)
            return quickSelect(arr, left, pivotIndex - 1, k);
        else
            return quickSelect(arr, pivotIndex + 1, right, k);
    }
    return -1;
}

int findKthSmallest(int arr[], int n, int k) {
    return quickSelect(arr, 0, n - 1, k - 1);
}

int main() {
    int arr[] = {7, 10, 4, 3, 20, 15};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3; // Find the 3rd smallest element

    printf("The %dth smallest element is: %d\n", k, findKthSmallest(arr, n, k));
    return 0;
}
