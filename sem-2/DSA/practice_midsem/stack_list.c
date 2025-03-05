#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void push(struct Node** top, int data);
void pop(struct Node** top);
void peek(struct Node* top);
int size(struct Node* top);
void isEmpty(struct Node* top);

void push(struct Node** top, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *top;
    *top = newNode;
}

void pop(struct Node** top) {
    if (*top == NULL) {
        printf("Stack is empty\n");
        return;
    }
    struct Node* temp = *top;
    printf("Popped element: %d\n", temp->data);
    *top = (*top)->next;
    free(temp);
}

void peek(struct Node* top) {
    if (top == NULL) {
        printf("Stack is empty\n");
    } else {
        printf("Top element: %d\n", top->data);
    }
}

int size(struct Node* top) {
    int count = 0;
    while (top != NULL) {
        count++;
        top = top->next;
    }
    return count;
}

void isEmpty(struct Node* top) {
    if (top == NULL) {
        printf("Stack is empty\n");
    } else {
        printf("Stack is not empty\n");
    }
}

int main() {
    struct Node* top = NULL;
    int choice, value;

    while (1) {
        printf("\n1. Push\n2. Pop\n3. Peek\n4. Size\n5. Is Empty\n6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter element to push: ");
                scanf("%d", &value);
                push(&top, value);
                break;
            case 2:
                pop(&top);
                break;
            case 3:
                peek(top);
                break;
            case 4:
                printf("Stack size: %d\n", size(top));
                break;
            case 5:
                isEmpty(top);
                break;
            case 6:
                return 0;
            default:
                printf("Invalid choice\n");
        }
    }
}
