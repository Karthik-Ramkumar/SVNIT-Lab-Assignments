#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *link;
};

void createList(struct node **head, int n);
void duplicateRemoval(struct node **head);
void displayList(struct node **head);

int main()
{
    struct node *head = NULL;
    int n = 0;

    printf("Enter number of elements in the node: ");
    scanf("%d", &n);
    createList(&head, n);

    // Displaying list after rotation
    displayList(&head);

    return 0;
}

void createList(struct node **head, int n)
{
    struct node *temp, *newNode;
    printf("Enter elements into the node: ");
    for (int i = 1; i <= n; i++)
    {
        int data;
        newNode = (struct node *)malloc(sizeof(struct node));
        scanf("%d", &data);
        newNode->data = data;
        newNode->link = NULL;
        
        if (*head == NULL)
        {
            *head = newNode;
            temp = newNode;
        }
        else
        {
            temp->link = newNode;
            temp = newNode;
        }
    }
}

void duplicateRemoval(struct node **head)
{

}

void displayList(struct node **head)
{
    struct node *p = head;
    printf("Rotated Linked List: ");
    while (p != NULL)
    {
        printf("%d ", p->data);
        p = p->link;
    }
    printf("NULL\n");
}
