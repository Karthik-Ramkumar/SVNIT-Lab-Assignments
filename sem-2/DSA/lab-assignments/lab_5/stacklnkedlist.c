#include <stdio.h>
#include <stdlib.h>

struct Node 
{
    int data;
    struct Node* next;
};

struct Stack 
{
    struct Node* top;
};

void create(struct Stack* s) 
{
    s->top = NULL;
}

int isEmpty(struct Stack* s) 
{
    return s->top == NULL;
}

void push(struct Stack* s, int value) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (!newNode) {
        printf("Heap overflow!\n");
        return;
    }
    newNode->data = value;
    newNode->next = s->top;
    s->top = newNode;
}

int pop(struct Stack* s) 
{
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    }
    struct Node* temp = s->top;
    int popped = temp->data;
    s->top = s->top->next;
    free(temp);
    return popped;
}

int peek(struct Stack* s) 
{
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return -1;
    }
    return s->top->data;
}

int main() 
{
    struct Stack s;
    create(&s);
    
    int choice, value;
    
    while (1) 
    {
        printf("\nStack Operations:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek\n");
        printf("4. Check if Empty\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) 
        {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(&s, value);
                break;
            case 2:
                printf("Popped: %d\n", pop(&s));
                break;
            case 3:
                printf("Top element: %d\n", peek(&s));
                break;
            case 4:
                printf("Stack empty: %s\n", isEmpty(&s) ? "Yes" : "No");
                break;
            case 5:
                printf("Exiting program...\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    
    return 0;
}
