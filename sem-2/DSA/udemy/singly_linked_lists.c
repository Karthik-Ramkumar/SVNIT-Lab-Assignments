#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *link;
};

struct node *createList()
{
    struct node *head = NULL, *temp = NULL, *newNode;
    int n, value, i;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        // Allocating space for each node
        newNode = (struct node *)malloc(sizeof(struct node));
        // Taking data input for each node
        printf("Enter value of node %d: ", i + 1);
        scanf("%d", &value);
        // Storing value into data part of struct
        newNode->data = value;
        newNode->link = NULL;

        // For inputting the first node
        if (head == NULL)
        {
            head = newNode;
        }
        // For subsequent nodes
        else
        {
            temp->link = newNode;
        }
        temp = newNode;
    }

    // Printing the list after creation
    printf("Linked list created: ");
    temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->link;
    }
    printf("\n");

    return head;
}

// Function to count the number of nodes
int countNodes(struct node *head)
{
    int count = 0;
    struct node *p = head;
    while (p != NULL)
    {
        count++;
        p = p->link;
    }
    return count;
}

// Function to find the position of a node containing specific data
int nodePosition(struct node *head, int value)
{
    int pos = 1;
    struct node *p = head;
    while (p != NULL)
    {
        if (p->data == value)
        {
            return pos;
        }
        p = p->link;
        pos++;
    }
    return -1; // Return -1 if the value is not found
}

// Function to insert a node in the list
void insertData(struct node **head, int position, int value)
{
    struct node *newNode, *p, *prev;
    p = *head;
    prev = NULL;
    int pos = 1;

    // Creating new node
    newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = value;
    newNode->link = NULL;

    // insertion into empty list
    if (*head == NULL && position == 1)
    {
        newNode->link = *head;
        *head = newNode;
    }

    // insertion at start
    else if (position == 1)
    {
        newNode->link = *head;
        *head = newNode;
    }

    // insertion at the end
    else if (position == countNodes(*head) + 1)
    {
        // Traverse to the last node
        while (p->link != NULL)
        {
            p = p->link;
        }
        // Insert new node at the end
        p->link = newNode;
    }
    else
    {
        // Insert before a node (in between the list)
        for (pos = 1; pos < position - 1 && p != NULL; pos++)
        {
            p = p->link;
        }

        // Insert new node after the predecessor node
        if (p != NULL)
        {
            newNode->link = p->link; // New node points to the next node
            p->link = newNode;       // Predecessor node points to the new node
        }
    }
}

void deleteNode(struct node **head, int position)
{
    struct node *temp = *head, *p = NULL;
    // If there's only one node in the list
    if (countNodes(*head) == 1 && position == 1)
    {
        temp = *head;
        *head = NULL;
        free(temp);
        return;
    }

    // Deleting the first node
    else if (position == 1)
    {
        temp = *head;
        *head = (*head)->link;
        free(temp);
        return;
    }

    // Deleting a node in the middle or end
    else if (position > 1)
    {
        p = *head;
        for (int i = 1; i < position-1 && p != NULL; i++) // need to get pointer to previous node
        {
            p = p->link;
        }
        if (p != NULL && p->link != NULL)
        {
            temp = p->link;
            p->link = temp->link;
            free(temp);
        }
        else
        {
            printf("Invalid position.\n");
        }
    }
}

int main()
{
    struct node *head = NULL;
    int choice;

    // Menu board
    printf("Select an option:\n");
    printf("1 - Create a linked list\n");
    printf("2 - Number of nodes in the list\n");
    printf("3 - Node position of specific data\n");
    printf("4 - Insterion of node\n");
    printf("5 - Delete a node\n");
    printf("99 - Exit\n");

    while (1)
    {
        printf("\nEnter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 99:
            printf("Exiting program...\n");
            return 0;

        case 1:
            head = createList();
            break;

        case 2:
            if (head == NULL)
            {
                printf("The list is empty. Create the list first.\n");
            }
            else
            {
                printf("Total number of nodes: %d\n", countNodes(head));
            }
            break;

        case 3:
            if (head == NULL)
            {
                printf("The list is empty. Create the list first.\n");
            }
            else
            {
                int value;
                printf("Enter data to search position: ");
                scanf("%d", &value);
                int position = nodePosition(head, value);
                if (position != -1)
                {
                    printf("%d is present at position %d.\n", value, position);
                }
                else
                {
                    printf("%d is not present in the list.\n", value);
                }
            }
            break;

        case 4:
            int pos, value;
            printf("Enter position where to enter: ");
            scanf("%d", &pos);
            printf("Enter value: ");
            scanf("%d", &value);
            insertData(&head, pos, value);

            // Printing the list after insertion
            printf("Linked list after insertion: ");
            struct node *temp = head;
            while (temp != NULL)
            {
                printf("%d ", temp->data);
                temp = temp->link;
            }
            printf("\n");
            break;

        case 5:
            if (head == NULL)
            {
                printf("The list is empty. Create the list first.\n");
            }
            else
            {
                int pos;
                printf("Enter the position of the node to delete: ");
                scanf("%d", &pos);

                if (pos < 1 || pos > countNodes(head))
                {
                    printf("Invalid position. Enter a valid position between 1 and %d.\n", countNodes(head));
                }
                else
                {
                    deleteNode(&head, pos);

                    // Printing the list after deletion
                    if (head == NULL)
                    {
                        printf("The list is now empty.\n");
                    }
                    else
                    {
                        printf("Linked list after deletion: ");
                        struct node *temp = head;
                        while (temp != NULL)
                        {
                            printf("%d ", temp->data);
                            temp = temp->link;
                        }
                        printf("\n");
                    }
                }
            }
            break;
        //switch bracket
        }
    }

    return 0;
}
