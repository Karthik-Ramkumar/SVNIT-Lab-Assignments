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
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    
    printf("Top element: %d\n", peek(&s));
    printf("Popped: %d\n", pop(&s));
    printf("Stack empty: %s\n", isEmpty(&s) ? "Yes" : "No");
    
    return 0;
}