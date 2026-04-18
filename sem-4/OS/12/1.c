#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_MEMORY 1024
#define MAX_PROCESSES 200
#define MAX_QUICK_CLASSES 5

typedef struct Block
{
    int start;
    int size;
    int free;
    int process_id;
    struct Block *next;
} Block;

typedef struct
{
    int success_count;
    int fail_count;
    int total_requests;
    int total_requested_memory;
    int total_allocated_memory;
    double total_allocation_time;
} Stats;

typedef struct
{
    int class_size;
    Block *blocks[200];
    int count;
} QuickClass;

QuickClass quick_classes[MAX_QUICK_CLASSES] = {
    {16, {NULL}, 0},
    {32, {NULL}, 0},
    {64, {NULL}, 0},
    {128, {NULL}, 0},
    {256, {NULL}, 0}};

Block *create_block(int start, int size, int free, int process_id)
{
    Block *new_block = (Block *)malloc(sizeof(Block));
    new_block->start = start;
    new_block->size = size;
    new_block->free = free;
    new_block->process_id = process_id;
    new_block->next = NULL;
    return new_block;
}

void reset_quick_fit()
{
    int i;
    for (i = 0; i < MAX_QUICK_CLASSES; i++)
    {
        quick_classes[i].count = 0;
    }
}

Block *initialize_memory()
{
    reset_quick_fit();
    return create_block(0, TOTAL_MEMORY, 1, -1);
}

void display_memory(Block *head)
{
    Block *temp = head;
    printf("\nMemory Layout:\n");
    printf("-------------------------------------------------\n");
    while (temp != NULL)
    {
        printf("[%4d - %4d] Size=%4d KB | %s",
               temp->start,
               temp->start + temp->size - 1,
               temp->size,
               temp->free ? "FREE " : "USED ");
        if (!temp->free)
            printf("| P%d", temp->process_id);
        printf("\n");
        temp = temp->next;
    }
    printf("-------------------------------------------------\n");
}

void split_block(Block *block, int size, int process_id)
{
    if (block->size > size)
    {
        Block *new_block = create_block(block->start + size, block->size - size, 1, -1);
        new_block->next = block->next;
        block->next = new_block;
        block->size = size;
    }
    block->free = 0;
    block->process_id = process_id;
}

void coalesce_free_blocks(Block *head)
{
    Block *temp = head;
    while (temp != NULL && temp->next != NULL)
    {
        if (temp->free && temp->next->free)
        {
            Block *to_delete = temp->next;
            temp->size += to_delete->size;
            temp->next = to_delete->next;
            free(to_delete);
        }
        else
        {
            temp = temp->next;
        }
    }
}

Block *find_first_fit(Block *head, int size)
{
    Block *temp = head;
    while (temp != NULL)
    {
        if (temp->free && temp->size >= size)
            return temp;
        temp = temp->next;
    }
    return NULL;
}

Block *find_next_fit(Block *head, int size, Block **last_alloc)
{
    Block *start;
    Block *temp;

    if (*last_alloc == NULL)
        *last_alloc = head;

    start = *last_alloc;
    temp = start;

    while (temp != NULL)
    {
        if (temp->free && temp->size >= size)
        {
            *last_alloc = temp;
            return temp;
        }
        temp = temp->next;
    }

    temp = head;
    while (temp != start)
    {
        if (temp->free && temp->size >= size)
        {
            *last_alloc = temp;
            return temp;
        }
        temp = temp->next;
    }

    return NULL;
}

Block *find_best_fit(Block *head, int size)
{
    Block *temp = head;
    Block *best = NULL;

    while (temp != NULL)
    {
        if (temp->free && temp->size >= size)
        {
            if (best == NULL || temp->size < best->size)
                best = temp;
        }
        temp = temp->next;
    }
    return best;
}

Block *find_worst_fit(Block *head, int size)
{
    Block *temp = head;
    Block *worst = NULL;

    while (temp != NULL)
    {
        if (temp->free && temp->size >= size)
        {
            if (worst == NULL || temp->size > worst->size)
                worst = temp;
        }
        temp = temp->next;
    }
    return worst;
}

void rebuild_quick_fit(Block *head)
{
    int i;
    Block *temp;

    for (i = 0; i < MAX_QUICK_CLASSES; i++)
        quick_classes[i].count = 0;

    temp = head;
    while (temp != NULL)
    {
        if (temp->free)
        {
            for (i = 0; i < MAX_QUICK_CLASSES; i++)
            {
                if (temp->size == quick_classes[i].class_size && quick_classes[i].count < 200)
                {
                    quick_classes[i].blocks[quick_classes[i].count++] = temp;
                    break;
                }
            }
        }
        temp = temp->next;
    }
}

Block *find_quick_fit(Block *head, int size)
{
    int i, j;
    rebuild_quick_fit(head);

    for (i = 0; i < MAX_QUICK_CLASSES; i++)
    {
        if (quick_classes[i].class_size == size)
        {
            for (j = 0; j < quick_classes[i].count; j++)
            {
                if (quick_classes[i].blocks[j]->free)
                    return quick_classes[i].blocks[j];
            }
        }
    }

    return find_first_fit(head, size);
}

int allocate_memory(Block *head, int strategy, int size, int process_id, Block **last_alloc, Stats *stats)
{
    Block *target = NULL;
    clock_t start_time, end_time;
    double elapsed;

    start_time = clock();

    if (strategy == 1)
        target = find_first_fit(head, size);
    else if (strategy == 2)
        target = find_next_fit(head, size, last_alloc);
    else if (strategy == 3)
        target = find_best_fit(head, size);
    else if (strategy == 4)
        target = find_worst_fit(head, size);
    else if (strategy == 5)
        target = find_quick_fit(head, size);

    if (target != NULL)
        split_block(target, size, process_id);

    end_time = clock();
    elapsed = ((double)(end_time - start_time)) / CLOCKS_PER_SEC;

    stats->total_requests++;
    stats->total_requested_memory += size;
    stats->total_allocation_time += elapsed;

    if (target != NULL)
    {
        stats->success_count++;
        stats->total_allocated_memory += size;
        return 1;
    }
    else
    {
        stats->fail_count++;
        return 0;
    }
}

int free_memory(Block *head, int process_id)
{
    Block *temp = head;
    while (temp != NULL)
    {
        if (!temp->free && temp->process_id == process_id)
        {
            temp->free = 1;
            temp->process_id = -1;
            coalesce_free_blocks(head);
            return 1;
        }
        temp = temp->next;
    }
    return 0;
}

int get_used_memory(Block *head)
{
    int used = 0;
    Block *temp = head;
    while (temp != NULL)
    {
        if (!temp->free)
            used += temp->size;
        temp = temp->next;
    }
    return used;
}

int get_free_memory(Block *head)
{
    int free_mem = 0;
    Block *temp = head;
    while (temp != NULL)
    {
        if (temp->free)
            free_mem += temp->size;
        temp = temp->next;
    }
    return free_mem;
}

int get_external_fragmentation(Block *head)
{
    int total_free = 0;
    int largest_free = 0;
    Block *temp = head;

    while (temp != NULL)
    {
        if (temp->free)
        {
            total_free += temp->size;
            if (temp->size > largest_free)
                largest_free = temp->size;
        }
        temp = temp->next;
    }

    return total_free - largest_free;
}

int count_free_blocks(Block *head)
{
    int count = 0;
    Block *temp = head;
    while (temp != NULL)
    {
        if (temp->free)
            count++;
        temp = temp->next;
    }
    return count;
}

void print_stats(Block *head, Stats stats)
{
    int used = get_used_memory(head);
    int free_mem = get_free_memory(head);
    int external_frag = get_external_fragmentation(head);
    double success_rate = 0.0;
    double utilization = 0.0;
    double avg_time = 0.0;

    if (stats.total_requests > 0)
        success_rate = ((double)stats.success_count / stats.total_requests) * 100.0;

    utilization = ((double)used / TOTAL_MEMORY) * 100.0;

    if (stats.total_requests > 0)
        avg_time = stats.total_allocation_time / stats.total_requests;

    printf("\n=============== STATISTICS ===============\n");
    printf("Total Requests         : %d\n", stats.total_requests);
    printf("Successful Allocations : %d\n", stats.success_count);
    printf("Failed Allocations     : %d\n", stats.fail_count);
    printf("Success Rate           : %.2f%%\n", success_rate);
    printf("Used Memory            : %d KB\n", used);
    printf("Free Memory            : %d KB\n", free_mem);
    printf("Memory Utilization     : %.2f%%\n", utilization);
    printf("External Fragmentation : %d KB\n", external_frag);
    printf("Free Block Count       : %d\n", count_free_blocks(head));
    printf("Average Allocation Time: %.8f sec\n", avg_time);
    printf("==========================================\n");
}

void free_all_blocks(Block *head)
{
    Block *temp;
    while (head != NULL)
    {
        temp = head;
        head = head->next;
        free(temp);
    }
}

void run_test_case(int strategy)
{
    Block *memory = initialize_memory();
    Block *last_alloc = NULL;
    Stats stats = {0, 0, 0, 0, 0, 0.0};

    int i;
    int test1[] = {64, 128, 32, 256, 16};
    int test1_n = 5;
    int random_sizes[25];

    printf("\n=========================================\n");
    if (strategy == 1)
        printf("Running FIRST FIT\n");
    else if (strategy == 2)
        printf("Running NEXT FIT\n");
    else if (strategy == 3)
        printf("Running BEST FIT\n");
    else if (strategy == 4)
        printf("Running WORST FIT\n");
    else if (strategy == 5)
        printf("Running QUICK FIT\n");
    printf("=========================================\n");

    printf("\n--- Test Case 1: Allocate 5 processes ---\n");
    for (i = 0; i < test1_n; i++)
    {
        if (allocate_memory(memory, strategy, test1[i], i + 1, &last_alloc, &stats))
            printf("Allocated P%d (%d KB)\n", i + 1, test1[i]);
        else
            printf("Failed P%d (%d KB)\n", i + 1, test1[i]);
        display_memory(memory);
    }

    printf("\n--- Test Case 2: Free some and reallocate ---\n");
    free_memory(memory, 2);
    printf("Freed P2\n");
    display_memory(memory);

    free_memory(memory, 4);
    printf("Freed P4\n");
    display_memory(memory);

    if (allocate_memory(memory, strategy, 100, 6, &last_alloc, &stats))
        printf("Allocated P6 (100 KB)\n");
    else
        printf("Failed P6 (100 KB)\n");
    display_memory(memory);

    if (allocate_memory(memory, strategy, 50, 7, &last_alloc, &stats))
        printf("Allocated P7 (50 KB)\n");
    else
        printf("Failed P7 (50 KB)\n");
    display_memory(memory);

    printf("\n--- Test Case 3: Stress test (25 random allocations) ---\n");
    srand((unsigned int)time(NULL) + strategy);

    for (i = 0; i < 25; i++)
    {
        random_sizes[i] = (rand() % 241) + 16;
        if (allocate_memory(memory, strategy, random_sizes[i], 100 + i, &last_alloc, &stats))
            printf("Allocated P%d (%d KB)\n", 100 + i, random_sizes[i]);
        else
            printf("Failed P%d (%d KB)\n", 100 + i, random_sizes[i]);

        if (i % 5 == 2)
        {
            int pid_to_free = 100 + (rand() % (i + 1));
            if (free_memory(memory, pid_to_free))
                printf("Freed P%d during stress test\n", pid_to_free);
        }
    }

    display_memory(memory);
    print_stats(memory, stats);
    free_all_blocks(memory);
}

int main()
{
    int choice;

    printf("Dynamic Memory Allocation Simulation\n");
    printf("Total Memory = %d KB\n", TOTAL_MEMORY);

    while (1)
    {
        printf("\nChoose Strategy:\n");
        printf("1. First Fit\n");
        printf("2. Next Fit\n");
        printf("3. Best Fit\n");
        printf("4. Worst Fit\n");
        printf("5. Quick Fit\n");
        printf("6. Run All\n");
        printf("0. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        if (choice == 0)
            break;
        else if (choice >= 1 && choice <= 5)
            run_test_case(choice);
        else if (choice == 6)
        {
            run_test_case(1);
            run_test_case(2);
            run_test_case(3);
            run_test_case(4);
            run_test_case(5);
        }
        else
            printf("Invalid choice\n");
    }

    return 0;
}