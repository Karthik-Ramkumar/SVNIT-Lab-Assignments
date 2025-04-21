#include <stdio.h>
int main(){
    int arr[] = {8,5,6,4,7,9,2,3,1,0};
    int n = 10;
    int min = 0;
    for(int i=0 ; i < n ; i++){
        int min = i;
        for(int j = i+1 ; j < n ; j++)
        {
            if(arr[j] < arr[min]){
                min = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
    for(int i = 0 ; i < n ; i++){
        printf("%d ", arr[i]);
        printf("\n");
    }
}