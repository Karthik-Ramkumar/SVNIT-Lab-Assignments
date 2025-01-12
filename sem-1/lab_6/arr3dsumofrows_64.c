#include <stdio.h>
int main()
{
    int arr[3][3];
    int total,x,y=0;
    printf("enter the numbers into the array");
    
    for(x = 0; x < 3; x++) 
    {
        for(y = 0; y < 3; y++) 
        {
            printf("Element at [%d][%d]: ", x, y);
            scanf("%d", &arr[x][y]);
            printf("%d",arr[x][y]);
        }
        
    }
    for(x=0;x<3;x++)
    {
        for(y=0;y<3;y++)
        {
             total = total+arr[x][y];
        }
        printf("sum of row %d = %d\t\n",x+1,total);
        total = 0;
    }
    return 0;
}