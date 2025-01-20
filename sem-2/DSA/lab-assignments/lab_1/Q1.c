#include <stdio.h>
int main()
{
    int n = 0;
    //Taking input
    printf("enter how many elements:");
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements: \n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    int max = arr[0]; //Initializing max element to 0th index
    for (int i = 1; i < n; i++)
    {
        if (arr[i] > max)
        {
            max = arr[i];
        }
        else if (arr[i] < arr[i - 1])
        {
            break;
        }
    }
    printf("The maximum element is: %d\n", max);
    return 0;
}