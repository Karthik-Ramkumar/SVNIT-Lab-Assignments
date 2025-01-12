#include<stdio.h>
int max(int a[],int n);
int main(){
int n;
printf("enter a length of n:");
scanf("%d",&n);
int a[n];
printf("enter elements of array");
for(int i=0;i<n;i++)
{
    scanf("%d",&a[i]);
}
printf("max from entered elements is:%d",max(a,n));
    return 0;
}
int max(int a[],int n)
{
    int maximum=-2147483648;
    for (int i = 0; i < n; i++)
    {
        if(a[i]>maximum){
            maximum=a[i];
        }
    }
    return maximum;
    
}