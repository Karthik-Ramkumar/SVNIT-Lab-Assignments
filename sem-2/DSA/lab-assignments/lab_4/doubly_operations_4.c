#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node *prev;
    int data;
    struct node *next;
};
void insert_element(struct node **head);
void insertBeginning(struct node **head, int data);
void insertAfterNode(struct node **head, int value, int data);
void insertEnd(struct node **head, int data);
void insertAtMiddle(struct node **head, int data);
void displayList(struct node **head);

int main()
{
    struct node *head = NULL;
    insert_element(&head);
    struct node *ptr = head;
    printf("--Enter Choice--\n");
    printf("1- instert beggining\n");
    printf("2- insert after node\n");
    printf("3- insert end\n");
    printf("4- insert middle\n");
    int data;
    int n;
    scanf("%d",&n);
    switch(n)
    {
        case 1:
        printf("Enter data to insert in node\n");
        scanf("%d",&data);
        insertBeginning(&head,data);
        displayList(&head);

        case 2:
        int value;
        printf("Enter data to insert in node\n");
        scanf("%d",&data);
        printf("Enter after which node to insert\n");
        scanf("%d",&value);
        insertAfterNode(&head,value,data);
        displayList(&head);

        case 3:
        printf("Enter data to insert in node\n");
        scanf("%d",&data);
        insertEnd(&head,data);
        displayList(&head);

        case 4:
        printf("Enter data to insert in node\n");
        scanf("%d",&data);
        insertAtMiddle(&head,data);
        displayList(&head);

    }
}
void displayList(struct node **head) 
{
    struct node *temp = *head;

    if (head == NULL) 
    {
        printf("List is empty\n");
        return;
    }

    while (temp != NULL) 
    {
        printf("%d", temp->data);
        if (temp->next != NULL) 
        {
            printf("<->");
        }
        temp = temp->next;
    }
    printf("\n");
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

void insertBeginning(struct node **head, int data) 
{
    struct node *newNode = (struct node *)malloc(sizeof(struct node));

    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = *head;

    if (*head != NULL) 
    {
        (*head)->prev = newNode;
    }

    *head = newNode;
}

void insertEnd(struct node **head, int data) 
{
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    struct node *temp = *head;

    newNode->data = data;
    newNode->next = NULL;

    while (temp->next != NULL) 
    {
        temp = temp->next;
    }

    newNode->prev = temp;
    temp->next = newNode;
}

void insertAfterNode(struct node **head, int position, int data) 
{
    struct node *temp = *head;

    for (int i = 1; temp != NULL && i < position; i++) 
    {
        temp = temp->next;
    }

    if (temp != NULL) 
    {
        struct node *newNode = (struct node *)malloc(sizeof(struct node));
        newNode->data = data;

        newNode->next = temp->next;
        newNode->prev = temp;

        if (temp->next != NULL) 
        {
            temp->next->prev = newNode;
        }

        temp->next = newNode;
    } 
    else 
    {
        printf("Position %d is out of range\n", position);
    }
}

void insertAtMiddle(struct node **head, int data) 
{

    struct node *temp = *head;
    int count = 0;

    while (temp != NULL) 
    {
        count++;
        temp = temp->next;
    }

    int mid = count / 2;
    temp = *head;

    for (int i = 0; i < mid; i++) 
    {
        temp = temp->next;
    }

    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->next = temp->next;
    newNode->prev = temp;

    if (temp->next != NULL) 
    {
        temp->next->prev = newNode;
    }

    temp->next = newNode;
}
