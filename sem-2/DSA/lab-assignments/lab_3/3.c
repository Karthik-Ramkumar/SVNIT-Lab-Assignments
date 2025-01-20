#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};


void traverse(struct node *head) 
{
    struct node *ptr = head;
    while (ptr != NULL) 
    {
        printf("%d -> ", ptr->data);
        ptr = ptr->next;
    }
    printf("NULL\n");
}


void insert_end(struct node **head, int value) 
{
    struct node *new_node = (struct node*)malloc(sizeof(struct node));

    new_node->data = value;
    new_node->next = NULL;

    if (*head == NULL) 
    {
        *head = new_node;
    } 
    else 
    {
        struct node *ptr = *head;
        while (ptr->next != NULL) 
        {
            ptr = ptr->next;
        }
        ptr->next = new_node;
    }
}

int main() 
{
    struct node *head = NULL;
    int n, value;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) 
    {
        printf("Enter node data: ");
        scanf("%d", &value);
        insert_end(&head, value);
    }

    printf("Linked List: ");
    traverse(head);

    return 0;
}
