#include <stdio.h>
int main()
{
    int arr1[3][3];
    int arr2[3][3];
    int sum[3][3];
    int x,y=0;
    int a,b = 0;
    printf("enter the numbers into the first array\n");
    for(x = 0; x < 3; x++) 
    {
        for(y = 0; y < 3; y++) 
        {
            printf("Element at [%d][%d]: ", x, y);
            scanf("%d", &arr1[x][y]);
            printf("%d",arr1[x][y]);
        }
    }
    printf("enter the numbers into the second array\n");
    for(a = 0;a<3;a++)
    {
        for(b = 0;b<3;b++)
        {
            printf("Element at [%d][%d]: ", a,b);
            scanf("%d", &arr2[a][b]);
            printf("%d",arr2[a][b]);        
        }
    }
    printf("\n");

    //---------- now adding the arrays
    for(int i = 0;i<3;i++)
    {
        for(int j = 0;j<3;j++)
        {
            sum[i][j] = arr1[i][j]*arr2[i][j];
        }
    }

    //--------- printing the sum array
    for(int k = 0;k<3;k++)
    {
        for(int l = 0;l<3;l++)
        {
            printf("%d\t",sum[k][l]);
        }
        printf("\n");
    }
    return 0;




}