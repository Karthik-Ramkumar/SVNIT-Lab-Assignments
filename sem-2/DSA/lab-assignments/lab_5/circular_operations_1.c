#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void displayList(struct node *last);
struct node *insertAtBeginning(struct node **last, int data);
struct node *insertAtEnd(struct node **last, int data);
void deleteFirstNode(struct node **last);
void deleteLastNode(struct node **last);
void deleteNode(struct node **last, int position);
void createList(struct node **last);
void insertNode(struct node **last, int data, int position);

void displayList(struct node *last) 
{
    if (last == NULL) 
    {
        printf("List is empty.\n");
        return;
    }
    struct node *temp = last->next;
    do 
    {
        printf("%d -> ", temp->data);
        temp = temp->next;
    } 
    while (temp != last->next);
    printf("(Back to start)\n");
}

void createList(struct node **last) 
{
    *last = NULL;
    printf("Circular linked list created.\n");
}

struct node *insertAtBeginning(struct node **last, int data) 
{
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    
    if (*last == NULL) 
    {
        newNode->next = newNode;
        *last = newNode;
    }
     else 
     {
        newNode->next = (*last)->next;
        (*last)->next = newNode;
    }
    return *last;
}

struct node *insertAtEnd(struct node **last, int data) 
{
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    
    if (*last == NULL) 
    {
        newNode->next = newNode;
        *last = newNode;
    } 
    else 
    {
        newNode->next = (*last)->next;
        (*last)->next = newNode;
        *last = newNode;
    }
    return *last;
}

void insertNode(struct node **last, int data, int position) 
{
    if (position == 0) 
    {
        insertAtBeginning(last, data);
    } 
    else 
    {
        struct node *temp = (*last)->next;
        for (int i = 0; i < position - 1 && temp != *last; i++) 
        {
            temp = temp->next;
        }
        struct node *newNode = (struct node *)malloc(sizeof(struct node));
        newNode->data = data;
        newNode->next = temp->next;
        temp->next = newNode;
        if (temp == *last) 
        {
            *last = newNode;
        }
    }
}

void deleteFirstNode(struct node **last) 
{
    if (*last == NULL) 
    {
        printf("List is empty.\n");
        return;
    }
    struct node *temp = (*last)->next;
    if (*last == temp) 
    {
        free(temp);
        *last = NULL;
    } 
    else 
    {
        (*last)->next = temp->next;
        free(temp);
    }
}

void deleteLastNode(struct node **last) 
{
    if (*last == NULL) 
    {
        printf("List is empty.\n");
        return;
    }
    struct node *temp = (*last)->next;
    if (*last == temp) 
    {
        free(temp);
        *last = NULL;
    } 
    else 
    {
        while (temp->next != *last) 
        {
            temp = temp->next;
        }
        temp->next = (*last)->next;
        free(*last);
        *last = temp;
    }
}

void deleteNode(struct node **last, int position) 
{
    if (*last == NULL) 
    {
        printf("List is empty.\n");
        return;
    }
    if (position == 0) 
    {
        deleteFirstNode(last);
        return;
    }
    struct node *temp = (*last)->next, *prev;
    for (int i = 0; i < position - 1 && temp != *last; i++) 
    {
        prev = temp;
        temp = temp->next;
    }
    if (temp == *last) 
    {
        deleteLastNode(last);
    } 
    else 
    {
        prev->next = temp->next;
        free(temp);
    }
}

int main() 
{
    struct node *last = NULL;
    int choice;

    while (1) 
    {
        printf("\n1 - Create list\n");
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
            {
                int position;
                printf("Enter position to delete: ");
                scanf("%d", &position);
                deleteNode(&last, position);
                displayList(last);
                break;
            }
            case 99:
                printf("Exiting program...\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}
