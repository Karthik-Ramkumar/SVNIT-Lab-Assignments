#include <stdio.h>
#include <string.h>

#define MAX_PROCESSES 10
#define TOTAL_MEMORY 1000

struct Segment
{
    char name[20];
    int size;
    int base;
    int allocated;
};

struct Process
{
    int processId;
    struct Segment code;
    struct Segment data;
    struct Segment stack;
    int active;
};

int main()
{
    struct Process processes[MAX_PROCESSES];
    int i;

    int memoryUsed = 0;
    int choice;
    int processId;
    int codeSize, dataSize, stackSize;
    int totalRequired;
    int found;

    for (i = 0; i < MAX_PROCESSES; i++)
    {
        processes[i].active = 0;
    }

    while (1)
    {
        printf("\n--- Segmentation Memory Management ---\n");
        printf("1. Create Process and Allocate Segments\n");
        printf("2. Deallocate Process Segments\n");
        printf("3. Display Process Segment Table\n");
        printf("4. Display Memory Status\n");
        printf("5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        if (choice == 1)
        {
            found = -1;

            for (i = 0; i < MAX_PROCESSES; i++)
            {
                if (processes[i].active == 0)
                {
                    found = i;
                    break;
                }
            }

            if (found == -1)
            {
                printf("No free process slot available.\n");
                continue;
            }

            printf("Enter Process ID: ");
            scanf("%d", &processId);

            for (i = 0; i < MAX_PROCESSES; i++)
            {
                if (processes[i].active == 1 && processes[i].processId == processId)
                {
                    printf("Process ID already exists.\n");
                    found = -1;
                    break;
                }
            }

            if (found == -1)
            {
                continue;
            }

            printf("Enter Code Segment Size: ");
            scanf("%d", &codeSize);

            printf("Enter Data Segment Size: ");
            scanf("%d", &dataSize);

            printf("Enter Stack Segment Size: ");
            scanf("%d", &stackSize);

            totalRequired = codeSize + dataSize + stackSize;

            if (memoryUsed + totalRequired > TOTAL_MEMORY)
            {
                printf("Not enough memory to allocate process.\n");
                continue;
            }

            processes[found].processId = processId;
            processes[found].active = 1;

            strcpy(processes[found].code.name, "Code");
            processes[found].code.size = codeSize;
            processes[found].code.base = memoryUsed;
            processes[found].code.allocated = 1;
            memoryUsed = memoryUsed + codeSize;

            strcpy(processes[found].data.name, "Data");
            processes[found].data.size = dataSize;
            processes[found].data.base = memoryUsed;
            processes[found].data.allocated = 1;
            memoryUsed = memoryUsed + dataSize;

            strcpy(processes[found].stack.name, "Stack");
            processes[found].stack.size = stackSize;
            processes[found].stack.base = memoryUsed;
            processes[found].stack.allocated = 1;
            memoryUsed = memoryUsed + stackSize;

            printf("Process %d created successfully.\n", processId);
            printf("Code  -> Base: %d, Size: %d\n", processes[found].code.base, processes[found].code.size);
            printf("Data  -> Base: %d, Size: %d\n", processes[found].data.base, processes[found].data.size);
            printf("Stack -> Base: %d, Size: %d\n", processes[found].stack.base, processes[found].stack.size);
        }
        else if (choice == 2)
        {
            printf("Enter Process ID to deallocate: ");
            scanf("%d", &processId);

            found = -1;

            for (i = 0; i < MAX_PROCESSES; i++)
            {
                if (processes[i].active == 1 && processes[i].processId == processId)
                {
                    found = i;
                    break;
                }
            }

            if (found == -1)
            {
                printf("Process not found.\n");
            }
            else
            {
                memoryUsed = memoryUsed - processes[found].code.size;
                memoryUsed = memoryUsed - processes[found].data.size;
                memoryUsed = memoryUsed - processes[found].stack.size;

                processes[found].active = 0;

                printf("Process %d deallocated successfully.\n", processId);
                printf("Note: This is a simple simulation. Memory holes are not compacted.\n");
            }
        }
        else if (choice == 3)
        {
            printf("\n--- Process Segment Tables ---\n");

            for (i = 0; i < MAX_PROCESSES; i++)
            {
                if (processes[i].active == 1)
                {
                    printf("\nProcess ID: %d\n", processes[i].processId);
                    printf("Segment\tBase\tSize\n");
                    printf("%s\t%d\t%d\n", processes[i].code.name, processes[i].code.base, processes[i].code.size);
                    printf("%s\t%d\t%d\n", processes[i].data.name, processes[i].data.base, processes[i].data.size);
                    printf("%s\t%d\t%d\n", processes[i].stack.name, processes[i].stack.base, processes[i].stack.size);
                }
            }
        }
        else if (choice == 4)
        {
            printf("\nTotal Memory     : %d\n", TOTAL_MEMORY);
            printf("Used Memory      : %d\n", memoryUsed);
            printf("Available Memory : %d\n", TOTAL_MEMORY - memoryUsed);
        }
        else if (choice == 5)
        {
            break;
        }
        else
        {
            printf("Invalid choice.\n");
        }
    }

    return 0;
}