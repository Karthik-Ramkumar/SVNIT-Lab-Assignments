#include <stdio.h>
int main() 
{
    int arr[] = {5, 4, 3, 2, 1};
    int n = 5;
    
    for(int i = 0; i < n - 1; i++)  // Outer loop
    {
        for(int j = i + 1; j < n; j++)  // Inner loop
        {
            if(arr[i] > arr[j])  // Swap if out of order
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    
    for(int i = 0; i < n; i++) // Print sorted array
    {
        printf("%d ", arr[i]);
    }
    
    return 0;
}
