#include <stdio.h>
int main()
{
    int arr[10] = {5,654,54,82,1,0,54,87,75,10};
    int input;
    int flag = 1;
    printf("enter the element u wanto search in array\n");
    scanf("%d",&input);
    for(int i = 0;i<10;i++)
    {
        if(arr[i]==input)
        {
            printf("element is there in the array");
            break;
            flag = 0;
        }
        
    }
    if(flag == 1)
    {
        printf("element not there in the array\n");
    }
    return 0;
}