// if list empty and we need to add -> front = temp; rear = temp;
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node *front = NULL, *rear = NULL;

void enqueue(int data) 
{
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    
    if (rear == NULL) {
        front = rear = newNode;
    } 
    else 
    {
        rear->next = newNode;
        rear = newNode;
    }
}

void dequeue() {
    if (front == NULL) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* temp = front;
    printf("Deleted: %d\n", front->data);
    front = front->next;
    free(temp);
    
    if (front == NULL) rear = NULL; // Reset when last element is deleted
}

void peek() {
    if (front == NULL)
    {
        printf("Queue is empty\n");
    }
    else printf("Front element: %d\n", front->data);
}

int main() {
    enqueue(1);
    enqueue(2);
    peek();
    dequeue();
    dequeue();
    dequeue();  // Checking reset condition
    isFull();
    return 0;
}
