#include<stdio.h>
#include<stdlib.h>
int main()
{
int n;
printf("how many numbers you want to enter:");
scanf("%d",&n);
int a[n];
printf("enter your numbers:\n");
for(int i=0;i<n;i++)
{
    scanf("%d",&a[i]);
}

for(int j=0;j<n;j++)
{
    int b[3]={0,1,1};
    for(int k=2;k<100;k++)
    {
        int temp = b[0];
        b[0]=b[1];
        b[1]=b[2];
        b[2]=b[1]+b[0];

        if(b[2]==a[j]||a[j]==1||a[j]==0)
        {
            printf("is fib...\n");
            break;
        }
        if(b[2]>a[j])
        {
            printf("is not fib...\n");
            break;
        }   
    }
}
return 0;
}