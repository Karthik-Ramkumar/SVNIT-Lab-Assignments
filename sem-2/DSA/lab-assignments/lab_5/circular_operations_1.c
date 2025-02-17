#include <stdio.h>

void displayList(struct node *last);
struct node *insertAtBeginning(struct node **last, int data);
struct node *insertAtEnd(struct node **last, int data);
void deleteFirstNode(struct node **head);
void deleteLastNode(struct node **head);
void deleteNode(struct node **head, int position);


int main() 
{
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
// .