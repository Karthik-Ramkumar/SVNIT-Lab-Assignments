#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* last = NULL;

void insert(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;

    if (last == NULL) {  // First node
        last = newNode;
        last->next = last;
    } else {
        newNode->next = last->next;
        last->next = newNode;
        last = newNode;
    }
}

void deleteFront() {
    if (last == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node* temp = last->next;  // First node
    if (last == temp) {  // Only one node
        last = NULL;
    } else {
        last->next = temp->next;
    }
    printf("Deleted: %d\n", temp->data);
    free(temp);
}

void display() {
    if (last == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node* temp = last->next;
    do {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } while (temp != last->next);
    printf("(Back to start)\n");
}

int main() {
    insert(10);
    insert(20);
    insert(30);
    display();
    deleteFront();
    display();
    return 0;
}
