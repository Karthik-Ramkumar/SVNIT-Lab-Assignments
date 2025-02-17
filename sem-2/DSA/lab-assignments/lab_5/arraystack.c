#include <stdio.h>
#define MAX 100

int stack[MAX];
int top = -1;

void create() {
    top = -1;
}

void push(int value) {
    if (top == MAX - 1) {
        printf("Stack overflow\n");
        return;
    }
    stack[++top] = value;
}

int pop() {
    if (top == -1) {
        printf("Stack underflow\n");
        return -1;
    }
    return stack[top--];
}

int peek() {
    if (top == -1) {
        printf("Stack empty\n");
        return -1;
    }
    return stack[top];
}

int isFull() {
    return top == MAX - 1;
}

int isEmpty() {
    return top == -1;
}

int main() {
    int choice, value;
    create();

    while (1) {
        printf("\n1. Push\n2. Pop\n3. Peek\n4. Check if Full\n5. Check if Empty\n6. Exit\nEnter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to push: ");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                printf("Popped element: %d\n", pop());
                break;
            case 3:
                printf("Top element: %d\n", peek());
                break;
            case 4:
                printf("Stack full: %s\n", isFull() ? "Yes" : "No");
                break;
            case 5:
                printf("Stack empty: %s\n", isEmpty() ? "Yes" : "No");
                break;
            case 6:
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }
}
