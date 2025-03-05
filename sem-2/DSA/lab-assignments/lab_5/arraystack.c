#include <stdio.h>
#define MAX 50

void push(int arr[], int *top);
void pop(int arr[], int *top);
void peek(int arr[], int *top);
int size(int *top);
void isfull(int *top);
void isempty(int *top);

int main()
{
    int arr[MAX];
    int top = -1;
    int choice;

    while (1)
    {
        printf("\n1. Push\n2. Pop\n3. Peek\n4. Size\n5. Is Full\n6. Is Empty\n7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
            case 1: push(arr, &top); break;
            case 2: pop(arr, &top); break;
            case 3: peek(arr, &top); break;
            case 4: printf("Stack size: %d\n", size(&top)); break;
            case 5: isfull(&top); break;
            case 6: isempty(&top); break;
            case 7: return 0;
            default: printf("Invalid choice\n");
        }
    }
}

void push(int arr[], int *top)
{
    if (*top == MAX - 1)
    {
        printf("Stack is full\n");
        return;
    }
    printf("Enter element to push: ");
    (*top)++;
    scanf("%d", &arr[*top]);
}

void pop(int arr[], int *top)
{
    if (*top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Popped element: %d\n", arr[*top]);
        (*top)--;
    }
}

void peek(int arr[], int *top)
{
    if (*top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Top element: %d\n", arr[*top]);
    }
}

int size(int *top)
{
    return (*top) + 1;
}

void isfull(int *top)
{
    if (*top == MAX - 1)
    {
        printf("Stack is full\n");
    }
    else
    {
        printf("Not full\n");
    }
}

void isempty(int *top)
{
    if (*top == -1)
    {
        printf("Stack is empty\n");
    }
    else
    {
        printf("Not empty\n");
    }
}
