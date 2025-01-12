#include <stdio.h>
int main()
{
    int arr[3][3],x,y;
    int input;
    int count;
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
    printf("enter the element to find occurence for in the array");
    scanf("%d",&input);

    for(x = 0; x < 3; x++) 
    {
        for(y = 0; y < 3; y++) 
        {
            if(arr[x][y]==input)
            {
                count++;
            }    
        }
        
    }
    printf("number of occurence of the element is %d",count);
    return 0;

}