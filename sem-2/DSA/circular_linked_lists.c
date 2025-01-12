#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *link;
};

// Prototypes
void createList(struct node **last);
void insertNode(struct node **last, int data, int position);
void deleteNode(struct node **last);
void displayList(struct node *last);

int main() {
    struct node *last = NULL;
    int choice;

    while (1) {
        printf("\n 1 - Create list\n");
        printf("2 - Insert node\n");
        printf("3 - Delete a node\n");
        printf("99 - Quit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) 
        {
            case 1:
                createList(&last);
                displayList(last);
                break;

            case 2: 
            {
                int data, position;
                printf("Enter data and position: ");
                scanf("%d %d", &data, &position);
                insertNode(&last, data, position);
                displayList(last);
                break;
            }

            case 3:
                deleteNode(&last);
                displayList(last);
                break;

            case 99:
                printf("Exiting program...\n");
                return 0;

            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}

void createList(struct node **last) 
{
    int n, data;
    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter data for node %d: ", i + 1);
        scanf("%d", &data);
        if (*last == NULL) 
        {
            struct node *insertIntoEmptyList(struct node **last, int data);
            insertIntoEmptyList(last, data);
        } 
        else 
        {
            struct node *insertAtEnd(struct node **last, int data);
            insertAtEnd(last, data);
        }
    }
}

void insertNode(struct node **last, int data, int position) 
{
    struct node *insertIntoEmptyList(struct node **last, int data);
    struct node *insertAtBeginning(struct node **last, int data);
    struct node *insertAfterNode(struct node *temp, int data);
    struct node *insertAtEnd(struct node **last, int data);

    if (*last == NULL) {
        insertIntoEmptyList(last, data);
    } else if (position == 1) {
        insertAtBeginning(last, data);
    } else {
        struct node *temp = (*last)->link;
        int count = 1;

        while (count < position - 1 && temp != *last) {
            temp = temp->link;
            count++;
        }

        if (temp == *last && count < position - 1) {
            printf("Invalid position.\n");
        } else {
            insertAfterNode(temp, data);
        }
    }
}

void deleteNode(struct node **last) 
{
    struct node *deleteBeginning(struct node **last);
    struct node *deleteEnd(struct node **last);
    struct node *deleteAtPosition(struct node **last, int position);

    int position;
    printf("Enter the position of the node to delete: ");
    scanf("%d", &position);

    if (*last == NULL) {
        printf("List is empty. Nothing to delete.\n");
    } else if (position == 1) {
        deleteBeginning(last);
    } else {
        struct node *temp = (*last)->link;
        int count = 1;

        while (count < position - 1 && temp != *last) {
            temp = temp->link;
            count++;
        }

        if (temp == *last || temp->link == *last) {
            deleteEnd(last);
        } else if (count == position - 1) {
            deleteAtPosition(last, position);
        } else {
            printf("Invalid position.\n");
        }
    }
}

// Sub-functions 
struct node *insertIntoEmptyList(struct node **last, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->link = newNode;
    *last = newNode;
    return newNode;
}

struct node *insertAtEnd(struct node **last, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->link = (*last)->link;
    (*last)->link = newNode;
    *last = newNode;
    return newNode;
}

struct node *insertAtBeginning(struct node **last, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->link = (*last)->link;
    (*last)->link = newNode;
    return newNode;
}

struct node *insertAfterNode(struct node *temp, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->link = temp->link;
    temp->link = newNode;
    return newNode;
}

struct node *deleteBeginning(struct node **last) {
    struct node *temp = (*last)->link;
    if (*last == temp) {
        free(temp);
        *last = NULL;
    } else {
        (*last)->link = temp->link;
        free(temp);
    }
    return NULL;
}

struct node *deleteEnd(struct node **last) {
    struct node *temp = (*last)->link;

    if (*last == temp) {
        free(temp);
        *last = NULL;
    } else {
        while (temp->link != *last) {
            temp = temp->link;
        }
        temp->link = (*last)->link;
        free(*last);
        *last = temp;
    }
    return NULL;
}

struct node *deleteAtPosition(struct node **last, int position) {
    struct node *temp = (*last)->link;
    struct node *prev = NULL;

    for (int i = 1; i < position; i++) {
        prev = temp;
        temp = temp->link;
    }

    if (temp == *last) {
        deleteEnd(last);
    } else {
        prev->link = temp->link;
        free(temp);
    }
    return NULL;
}

void displayList(struct node *last) {
    if (last == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct node *temp = last->link;
    printf("List: ");
    do {
        printf("%d ", temp->data);
        temp = temp->link;
    } while (temp != last->link);
    printf("\n");
}
