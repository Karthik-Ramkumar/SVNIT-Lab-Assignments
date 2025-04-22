#include <stdio.h>

void binarySearch(int arr[], int left, int right, int target)
{
    if (left <= right) {
        int mid = (left + right) / 2;

        if (target == arr[mid]) {
            printf("Element found at index %d\n", mid);
            return;
        }
        else if (target < arr[mid]) {
            binarySearch(arr, left, mid - 1, target);
        }
        else {
            binarySearch(arr, mid + 1, right, target);
        }
    }
    else {
        printf("Element not found\n");
    }
}

int main()
{
    int arr[] = {2, 3, 4, 10, 40};
    int n = 5;
    int target = 2;
    binarySearch(arr, 0, n - 1, target);
}
// Time Complexity: O(log n)
// Space Complexity: O(1) for iterative, O(log n) for recursive