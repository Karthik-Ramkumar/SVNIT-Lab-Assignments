#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct CircularQueue {
    Node* rear; // We only need rear in a circular linked list queue
} CircularQueue;

Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void initializeQueue(CircularQueue* queue) {
    queue->rear = NULL;
}

int isEmpty(CircularQueue* queue) {
    return queue->rear == NULL;
}

void enqueue(CircularQueue* queue, int data) {
    Node* newNode = createNode(data);
    if (newNode == NULL) return;

    if (isEmpty(queue)) {
        queue->rear = newNode;
        queue->rear->next = newNode; // Circular link
    } else {
        newNode->next = queue->rear->next; // New node points to front
        queue->rear->next = newNode; // Old rear points to new node
        queue->rear = newNode; // Update rear
    }
    printf("%d enqueued to circular queue.\n", data);
}

int dequeue(CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Circular Queue is empty.\n");
        return -1; // Indicate error
    }

    Node* temp = queue->rear->next; // Front is rear->next
    int data = temp->data;

    if (queue->rear->next == queue->rear) { // Only one element
        queue->rear = NULL;
    } else {
        queue->rear->next = temp->next; // Remove front node
    }

    free(temp);
    printf("%d dequeued from circular queue.\n", data);
    return data;
}

int peek(CircularQueue* queue) {
    if (isEmpty(queue)) {
        printf("Circular Queue is empty.\n");
        return -1; // Indicate error
    }
    return queue->rear->next->data; // Front data
}

int isFull(CircularQueue* queue) {
    return 0; // Linked list queue is never truly full
}

void freeQueue(CircularQueue* queue) {
    if (isEmpty(queue)) return;

    Node* current = queue->rear->next;
    Node* temp;

    while (current != queue->rear) {
        temp = current;
        current = current->next;
        free(temp);
    }
    free(queue->rear);
    queue->rear = NULL;
}

int main() {
    CircularQueue cq;
    initializeQueue(&cq);

    int choice, data;

    while (1) {
        printf("\nCircular Queue Operations:\n");
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Peek\n");
        printf("4. Is Empty\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data: ");
                scanf("%d", &data);
                enqueue(&cq, data);
                break;
            case 2:
                dequeue(&cq);
                break;
            case 3:
                printf("Peek: %d\n", peek(&cq));
                break;
            case 4:
                if (isEmpty(&cq)) {
                    printf("Circular Queue is empty.\n");
                } else {
                    printf("Circular Queue is not empty.\n");
                }
                break;
            case 5:
                freeQueue(&cq);
                return 0;
            default:
                printf("Invalid choice!\n");
        }
    }

    return 0;
}