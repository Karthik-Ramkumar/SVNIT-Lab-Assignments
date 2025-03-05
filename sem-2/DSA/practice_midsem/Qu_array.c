// inserting -> increase rear and insert
// deleting -> delete front then increase
// number of elements in Queue is rear - front + 1
// Queue is empty when front = rear + 1
// Queue is full when rear = MAX - 1
#include <stdio.h>
#define MAX 5

int queue[MAX], front = -1, rear = -1;

void enqueue(int data) 
{
    if (rear == MAX - 1) 
    {
        printf("Queue is full\n");
        return;
    }
    if (front == -1)
    {
        front = 0;
    } 
    queue[++rear] = data;
}

void dequeue() 
{
    if (front == -1 || front > rear) 
        {
        printf("Queue is empty\n");
        front = rear = -1;
        return;
    }
    printf("Deleted: %d\n", queue[front++]);
}

void isFull() {
    printf(rear == MAX - 1 ? "Queue is full\n" : "Queue is not full\n");
}

void peek() {
    if (front == -1 || front > rear) printf("Queue is empty\n");
    else printf("Front element: %d\n", queue[front]);
}

int main() {
    enqueue(1);
    enqueue(2);
    peek();
    dequeue();
    isFull();
    return 0;
}
