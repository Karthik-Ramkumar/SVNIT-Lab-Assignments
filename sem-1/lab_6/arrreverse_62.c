#include <stdio.h>
int main()
{
    int arr[5] = {1,2,3,4,5};
    int temp[5] = {1,2,3,4,5};
    for(int i = 0;i<5;i++)
    {
        for(int j = 4;j>1;j--)
        {       
        arr[i] = temp[4-i];
        }
    }
    printf("array after reversing is: \n");
    for(int k = 0;k<5;k++)
    {
        printf("%d",arr[k]);
    }
    return 0;

}