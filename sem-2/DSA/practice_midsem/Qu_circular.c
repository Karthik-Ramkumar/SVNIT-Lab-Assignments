#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* rear = NULL;

void enqueue(int data) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;

    if (rear == NULL) {  // First node
        newNode->next = newNode;  // Points to itself
    } 
    else
    {
        newNode->next = rear->next;
        rear->next = newNode;
    }
    rear = newNode;  // Update rear
}

void dequeue() 
{
    if (rear == NULL) 
    {
        printf("Queue is empty\n");
        return;
    }

    struct Node* front = rear->next;  // Front node
    printf("Deleted: %d\n", front->data);

    if (rear == front) // Only one element
    {  
        rear = NULL;
    } 
    else
    {
        rear->next = front->next;
    }
    free(front);
}

void peek() {
    if (rear == NULL) printf("Queue is empty\n");
    else printf("Front element: %d\n", rear->next->data);
}

void display() {
    if (rear == NULL) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* temp = rear->next;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != rear->next);
    printf("(Back to front)\n");
}

int main() {
    enqueue(1);
    enqueue(2);
    enqueue(3);
    display();
    dequeue();
    peek();
    display();
    return 0;
}
