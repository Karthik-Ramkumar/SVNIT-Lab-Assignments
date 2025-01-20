#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void insert_element(struct node **head);
void insert_beginning(struct node **head);

int main() 
{
    struct node *head = NULL;
    insert_element(&head);

    struct node *ptr = head;
    //printing node
    while (ptr != NULL) 
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");
    insert_beginning(&head);
    ptr = head;
    while (ptr != NULL) 
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }

    return 0;
}

void insert_element(struct node **head) 
{
    struct node *new_node, *ptr;
    int n, nodes;

    printf("Enter number of nodes: ");
    scanf("%d", &nodes);

    for (int i = 0; i < nodes; i++) 
    {
        new_node = (struct node*)malloc(sizeof(struct node));

        printf("Enter node data: ");
        scanf("%d", &n);

        new_node->data = n;
        new_node->next = NULL;

        if (*head == NULL) 
        {
            *head = new_node;
        } 
        else 
        {
            ptr = *head;
            while (ptr->next != NULL) 
            {
                ptr = ptr->next;
            }
            ptr->next = new_node;
        }
    }
}

void insert_beginning(struct node **head)
{
    struct node *new,*ptr;
    new = (struct node*)malloc(sizeof(struct node));
    int n;
    printf("Enter data to insert at beggining of the list:\n");
    scanf("%d",&n);
    new -> data = n;
    new -> next = *head;
    *head = new;
}

