#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void insert(struct node **head);
void del(struct node **head);
void display(struct node *head);

int main() {
    struct node *head = NULL;
    int choice;
    while (1) {
        printf("\nMenu:\n1. Insert\n2. Delete\n3. Display\n4. Exit\nEnter choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                insert(&head);
                break;
            case 2:
                del(&head);
                break;
            case 3:
                display(head);
                break;
            case 4:
                exit(0);
            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}

void insert(struct node **head) {
    struct node *temp = (struct node *)malloc(sizeof(struct node));
    int data;
    printf("Enter element to insert: ");
    scanf("%d", &data);
    temp->data = data;
    temp->next = NULL;
    
    if (*head == NULL) 
    {
        *head = temp;
    } 
    else 
    {
        struct node *ptr = *head;
        while (ptr->next != NULL) 
        {
            ptr = ptr->next;
        }
        ptr->next = temp;
    }
    display(*head);
}

void del(struct node **head) 
{
    if (*head == NULL) 
    {
        printf("List is empty!\n");
        return;
    }
    
    int position;
    printf("Enter position to delete: ");
    scanf("%d", &position);
    
    struct node *ptr = *head, *prev = NULL;
    if (position == 0) 
    {
        *head = ptr->next;
        free(ptr);
    } 
    else 
    {
        while (position > 0 && ptr != NULL) {
            prev = ptr;
            ptr = ptr->next;
            position--;
        }
        if (ptr == NULL) 
        {
            printf("Invalid position!\n");
            return;
        }
        prev->next = ptr->next;
        free(ptr);
    }
    display(*head);
}

void display(struct node *head) {
    if (head == NULL) {
        printf("List is empty!\n");
        return;
    }
    struct node *ptr = head;
    printf("Linked List: ");
    while (ptr != NULL) {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}
