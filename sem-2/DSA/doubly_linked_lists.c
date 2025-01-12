#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node *prev;
    int data;
    struct node *next;
};

// Function prototypes
void insertEmpty(struct node **head, int data);
void insertEnd(struct node **head, int data);
void insertBeginning(struct node **head, int data);
void insertAfterNode(struct node *head, int value, int data);
void deleteOnlyNode(struct node **head);
void deleteFirstNode(struct node **head);
void deleteLastNode(struct node **head);
void deleteNode(struct node **head, int position);
void createList(struct node **head);
void displayList(struct node *head);

void insertEmpty(struct node **head, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    *head = newNode;
}

void insertBeginning(struct node **head, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));

    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = *head;

    if (*head != NULL) {
        (*head)->prev = newNode;
    }

    *head = newNode;
}

void insertEnd(struct node **head, int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    struct node *temp = *head;

    newNode->data = data;
    newNode->next = NULL;

    if (*head == NULL) {
        insertEmpty(head, data);
        return;
    }

    while (temp->next != NULL) {
        temp = temp->next;
    }

    newNode->prev = temp;
    temp->next = newNode;
}

void insertAfterNode(struct node *head, int value, int data) {
    struct node *temp = head;

    while (temp != NULL && temp->data != value) {
        temp = temp->next;
    }

    if (temp != NULL) {
        struct node *newNode = (struct node *)malloc(sizeof(struct node));
        newNode->data = data;
        newNode->next = temp->next;
        newNode->prev = temp;

        if (temp->next != NULL) {
            temp->next->prev = newNode;
        }

        temp->next = newNode;
    }
}

void deleteOnlyNode(struct node **head) {
    free(*head);
    *head = NULL;
}

void deleteFirstNode(struct node **head) {
    struct node *temp = *head;

    if (*head == NULL) return;

    *head = (*head)->next;
    if (*head != NULL) {
        (*head)->prev = NULL;
    }

    free(temp);
}

void deleteLastNode(struct node **head) {
    struct node *temp = *head;

    if (*head == NULL) return;

    while (temp->next != NULL) {
        temp = temp->next;
    }

    if (temp->prev != NULL) {
        temp->prev->next = NULL;
    } else {
        *head = NULL;
    }

    free(temp);
}

void deleteNode(struct node **head, int position) {
    int count = 1;
    struct node *temp = *head;

    while (temp != NULL && count < position) {
        temp = temp->next;
        count++;
    }

    if (temp == NULL) {
        printf("Invalid position.\n");
        return;
    }

    if (temp->prev != NULL) {
        temp->prev->next = temp->next;
    } else {
        *head = temp->next; // If it's the first node
    }

    if (temp->next != NULL) {
        temp->next->prev = temp->prev;
    }

    free(temp);
}

void createList(struct node **head) {
    int n, data, i;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("Enter data for node %d: ", i + 1);
        scanf("%d", &data);

        if (i == 0) {
            insertEmpty(head, data);
        } else {
            insertEnd(head, data);
        }
    }

    displayList(*head);
}

void displayList(struct node *head) {
    struct node *temp = head;

    printf("Current List: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    struct node *head = NULL;
    int choice;

    printf("Select an option: \n");
    printf("1 - Create a list\n");
    printf("2 - Insert a node\n");
    printf("3 - Delete a node\n");
    printf("99 - Exit\n");

    while (1) {
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                createList(&head);
                break;

            case 2: {
                int position, data, i = 1;
                struct node *temp = head;

                printf("Enter the position to insert: ");
                scanf("%d", &position);
                printf("Enter data: ");
                scanf("%d", &data);

                if (position == 1) {
                    insertBeginning(&head, data);
                } else {
                    while (i < position - 1 && temp != NULL) {
                        temp = temp->next;
                        i++;
                    }

                    if (temp != NULL) {
                        insertAfterNode(temp, temp->data, data);
                    } else {
                        printf("Invalid position.\n");
                    }
                }

                displayList(head);
                break;
            }

            case 3: {
                int position;
                printf("Enter the position to delete: ");
                scanf("%d", &position);

                if (head == NULL) {
                    printf("The list is empty.\n");
                } else if (head->next == NULL && position == 1) {
                    deleteOnlyNode(&head);
                } else if (position == 1) {
                    deleteFirstNode(&head);
                } else {
                    struct node *temp = head;
                    int count = 1;

                    while (temp->next != NULL) {
                        temp = temp->next;
                        count++;
                    }

                    if (position == count) {
                        deleteLastNode(&head);
                    } else if (position > 1 && position < count) {
                        deleteNode(&head, position);
                    } else {
                        printf("Invalid position.\n");
                    }
                }

                displayList(head);
                break;
            }

            case 99:
                printf("Exiting program...\n");
                return 0;

            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}
