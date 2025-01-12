#include <stdio.h>
int main()
{
    int arr1[10];
    int arr2[10];
    printf("enter the numbers for the first array \n");
    for(int i = 0;i<10;i++)
    {
        scanf("%d",&arr1[i]);
    }
    printf("enter the numbers for the second array \n");
    for(int j = 0;j<10;j++)
    {
        scanf("%d",&arr2[j]);
    }  
    int sum[10];
    for(int k = 0;k<10;k++)
    {
        sum[k] = arr1[k]+arr2[k];
    }  
    for(int m = 0;m<10;m++)
    {
        printf("%d \t\n",sum[m]);
    } 

    return 0;
}        
