//bubble sort
#include <stdio.h>
int main()
{
    int temp = 0;
    int arr[] = {5,6,4,2,9,1,3,8,7,0};
    for(int i = 0; i<10; i++)
    {
        for(int j = 0; j<9;j++)
        {
            if(arr[j]>arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
            
        }
    }
    for(int k =0; k<10; k++)
    {
        printf("%d \t",arr[k]);
    }
    return 0;
}