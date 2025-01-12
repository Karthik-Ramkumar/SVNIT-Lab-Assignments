#include <stdio.h>
int main()
{
    int arr1[5];
    int arr2[5];
    int temp[5];
    printf("enter the numbers for the first array \n");
    for(int i = 0;i<5;i++)
    {
        scanf("%d",&arr1[i]);
        temp[i] = arr1[i];
    }
    printf("enter the numbers for the second array \n");
    for(int j = 0;j<5;j++)
    {
        scanf("%d",&arr2[j]);
    }
    printf("\nfirst array is:  \n");
    for(int o = 0;o<5;o++)
    {
        printf("%d\t",arr1[o]);  //printing array 1
    }
    printf("\nsecond array is:  \n");
    for(int p = 0;p<5;p++)
    {
        printf("%d\t",arr2[p]); //printing array 2
    }
    //-------------------------------------------------------------


    for(int m = 0;m<5;m++)//assigning arr2 to 1
    {
        arr1[m]= arr2[m];       
    }
    for(int n = 0;n<5;n++)//assigning arr1 to 2 through temp
    {
        arr2[n]= temp[n];       
    }
    //----------------------------
    printf("\nfirst array after swap is:  \n");
    for(int x = 0;x<5;x++)
    {
        printf("%d\t",arr1[x]);   //printing array 1
    }
    printf("\nsecond array after swap is:  \n");
    for(int y= 0;y<5;y++)
    {
        printf("%d\t",arr2[y]);    //printing array 2
    }

    return 0;


}