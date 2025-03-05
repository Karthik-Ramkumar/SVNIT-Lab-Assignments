#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    int priority;
    struct Node* next;
} Node;

typedef struct PriorityQueue {
    Node* head;
} PriorityQueue;

Node* createNode(int data, int priority) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    newNode->data = data;
    newNode->priority = priority;
    newNode->next = NULL;
    return newNode;
}

void initializeQueue(PriorityQueue* pq) {
    pq->head = NULL;
}

int isEmpty(PriorityQueue* pq) {
    return pq->head == NULL;
}

void enqueue(PriorityQueue* pq, int data, int priority) {
    Node* newNode = createNode(data, priority);
    if (newNode == NULL) return;

    if (isEmpty(pq) || priority < pq->head->priority) {
        newNode->next = pq->head;
        pq->head = newNode;
    } else {
        Node* current = pq->head;
        while (current->next != NULL && current->next->priority <= priority) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
    printf("%d (Priority: %d) enqueued.\n", data, priority);
}

int dequeue(PriorityQueue* pq) {
    if (isEmpty(pq)) {
        printf("Priority Queue is empty.\n");
        return -1; // Indicate error
    }

    Node* temp = pq->head;
    int data = temp->data;
    pq->head = pq->head->next;
    free(temp);
    printf("%d dequeued.\n", data);
    return data;
}

int peek(PriorityQueue* pq) {
    if (isEmpty(pq)) {
        printf("Priority Queue is empty.\n");
        return -1; // Indicate error
    }
    return pq->head->data;
}

int isFull(PriorityQueue* pq) {
    return 0; // Linked list queue is never truly full
}

void freeQueue(PriorityQueue* pq) {
    while (!isEmpty(pq)) {
        dequeue(pq);
    }
}

int main() {
    PriorityQueue pq;
    initializeQueue(&pq);

    int choice, data, priority;

    while (1) {
        printf("\nPriority Queue Operations:\n");
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
                printf("Enter priority: ");
                scanf("%d", &priority);
                enqueue(&pq, data, priority);
                break;
            case 2:
                dequeue(&pq);
                break;
            case 3:
                printf("Peek: %d\n", peek(&pq));
                break;
            case 4:
                if (isEmpty(&pq)) {
                    printf("Priority Queue is empty.\n");
                } else {
                    printf("Priority Queue is not empty.\n");
                }
                break;
            case 5:
                freeQueue(&pq);
                return 0;
            default:
                printf("Invalid choice!\n");
        }
    }

    return 0;
}