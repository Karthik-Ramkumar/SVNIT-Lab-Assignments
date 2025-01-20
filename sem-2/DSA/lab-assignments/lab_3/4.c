#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

void insert_element(struct node **head, int *arr, int length);

int main() 
{
    int arr[] = {1, 2, 3, 4, 5};
    int length = sizeof(arr) / sizeof(arr[0]);  

    struct node *head = NULL;
    insert_element(&head, arr, length);  

    struct node *ptr = head;
    while (ptr != NULL) 
    {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }

    return 0;
}

void insert_element(struct node **head, int *arr, int length) 
{
    struct node *new_node, *ptr;

    for (int i = 0; i < length; i++) 
    {
        new_node = (struct node*)malloc(sizeof(struct node));
        if (new_node == NULL) 
        {
            printf("Memory allocation failed\n");
            return;
        }

        new_node->data = arr[i];
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
