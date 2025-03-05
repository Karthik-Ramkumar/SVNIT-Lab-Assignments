#include <stdio.h>
#define MAX 50
int main()
{
    int *arr[MAX];
    int *top = -1;
}
void push(int *arr,int *top)
{
    top += 1;
    printf("Enter element to push");
    scanf("%d",&arr[top]);
}

void pop(int *arr,int *top)
{
    if(top == -1)
    {
        printf("Stack is empty");
    }
    else
    {
        top += -1;
    }
}
void peek(int *arr,int *top)
{
    printf("%d",arr[top]);
}
void size(int *arr,int *top)
{
    return top+1;
}
void isfull(int *arr,int *top)
{
    if(top == MAX-1)
    {
        printf("FULL");
    }
    else {
        printf("Not full");
    }
}
void peek(int *arr, int *top)
{
    if (top == -1)
    {
        printf("stack empty");
    }
}