#include <stdio.h>

#define SIZE 9
#define BUCKETS 7

void bucket_sort(int arr[], int n) {
    int buckets[BUCKETS][SIZE], count[BUCKETS] = {0};
    int i, j, k;

    int max = arr[0], min = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }

    float range = (float)(max - min + 1) / BUCKETS;

    for (i = 0; i < n; i++) {
        int idx = (int)((arr[i] - min) / range);
        if (idx >= BUCKETS) idx = BUCKETS - 1;
        buckets[idx][count[idx]++] = arr[i];
    }

    for (i = 0; i < BUCKETS; i++) {
        for (j = 0; j < count[i] - 1; j++) {
            for (k = 0; k < count[i] - j - 1; k++) {
                if (buckets[i][k] > buckets[i][k + 1]) {
                    int temp = buckets[i][k];
                    buckets[i][k] = buckets[i][k + 1];
                    buckets[i][k + 1] = temp;
                }
            }
        }
    }

    k = 0;
    for (i = 0; i < BUCKETS; i++) {
        for (j = 0; j < count[i]; j++) {
            arr[k++] = buckets[i][j];
        }
    }
}

int main() {
    int arr[SIZE] = {12, 45, 33, 87, 56, 9, 11, 7, 67};
    int i;

    bucket_sort(arr, SIZE);

    for (i = 0; i < SIZE; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}
