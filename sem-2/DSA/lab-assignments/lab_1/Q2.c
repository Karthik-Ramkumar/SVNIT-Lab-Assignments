#include <stdio.h>
int invCount(int arr[], int n);
int main()
{
    int n,i,inversion = 0;
    //Taking input
    printf("enter how many elements:");
    scanf("%d", &n);
    int A[n];
    printf("Enter elements: \n");
    for (int k = 0; k < n; k++)
    {
        scanf("%d", &A[k]);
    }
    printf("number of inversions = %d \n", invCount(A, n));
    return 0;
}

int invCount(int arr[], int n) 
{
    int inversions = 0;
    for (int i = 0; i < n - 1; i++) 
    {
        for (int j = i + 1; j < n; j++) 
        {
            if (arr[i] > arr[j])
                inversions++;
        }
    }
    return inversions;
}