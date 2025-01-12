#include <stdio.h>
int main()
{
    int arr[10] = {5, 6, 7, 8, 2, 4, 1, 9, 3, 0};
    int temp = 0;
    int small_pos;

    for (int i = 0; i < 10; i++)
    {
        small_pos = i;
        for (int j = i + 1; j < 10; j++)
        {
            if(arr[j] < arr[small_pos])
            {
                small_pos = j;
            }
            if(small_pos != i)
            {
                temp = arr[i];
                arr[i] = arr[small_pos];
                arr[small_pos] = temp;
            }
        }
    }
    for (int k = 0; k < 10; k++)
    {
        printf("%d \t", arr[k]);
    }
    return 0;
}