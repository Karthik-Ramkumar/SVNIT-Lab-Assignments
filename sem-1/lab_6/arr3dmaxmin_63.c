#include <stdio.h>
int main()
{
    int arr[3][3],x,y;
    int max = -2147483647;
    int min = 2147483647;
    //---------entering array
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

    for(x = 0; x < 3; x++) 
    {
        for(y = 0; y < 3; y++) 
        {
                if(arr[x][y]>max)
                    {
                        max = arr[x][y];
                    }
                else if(arr[x][y]< min)
                    {
                        min = arr[x][y];
                    }            
        }   
    }
    printf("maximum number in the array = %d \n",max);
    printf("minimum number in the array = %d \n",min);
    return 0;
}