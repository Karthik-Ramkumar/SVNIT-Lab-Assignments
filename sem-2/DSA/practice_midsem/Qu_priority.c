#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data, priority;
    struct Node* next;
};

struct Node* front = NULL;

void enqueue(int data, int priority) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->priority = priority;
    newNode->next = NULL;

    if (front == NULL || priority < front->priority) {
        newNode->next = front;
        front = newNode;
    } 
    else 
    {
        struct Node* temp = front;
        while (temp->next != NULL && temp->next->priority <= priority) 
        {
            temp = temp->next;
        }
        newNode->next = temp->next;
        temp->next = newNode;
    }
}

void dequeue() {
    if (front == NULL) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* temp = front;
    front = front->next;
    free(temp);
}

void peek() {
    if (front == NULL) printf("Queue is empty\n");
    else printf("Front element: %d (Priority: %d)\n", front->data, front->priority);
}

void display() {
    if (front == NULL) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* temp = front;
    while (temp != NULL) {
        printf("%d (Priority: %d) -> ", temp->data, temp->priority);
        temp = temp->next;
    }
    printf("NULL\n");
}

int main() {
    enqueue(10, 2);
    enqueue(20, 1);
    enqueue(30, 3);
    display();
    dequeue();
    peek();
    display();
    return 0;
}
