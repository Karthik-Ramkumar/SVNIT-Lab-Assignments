#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100

typedef struct {
    char name[50];
    int rollNo;
    char department[50];
} Student;

void readFile(Student students[], int *n) {
    FILE *file = fopen("student.txt", "r");
    if (!file) {
        printf("Error opening file.\n");
        exit(1);
    }
    
    *n = 0;
    while (fscanf(file, "%[^,], %d, %s\n", students[*n].name, &students[*n].rollNo, students[*n].department) != EOF) {
        (*n)++;
        if (*n >= MAX_STUDENTS) break;
    }
    fclose(file);
}

void bubbleSort(Student students[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (strcmp(students[j].name, students[j + 1].name) > 0 || 
               (strcmp(students[j].name, students[j + 1].name) == 0 && students[j].rollNo > students[j + 1].rollNo)) {
                Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}

void binarySearch(Student students[], int n, char target[]) {
    int left = 0, right = n - 1, found = 0;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        int cmp = strcmp(students[mid].name, target);

        if (cmp == 0) {
            int i = mid;
            while (i >= 0 && strcmp(students[i].name, target) == 0) i--;
            i++;
            while (i < n && strcmp(students[i].name, target) == 0) {
                printf("%s, %d, %s\n", students[i].name, students[i].rollNo, students[i].department);
                found = 1;
                i++;
            }
            break;
        } 
        else if (cmp < 0) left = mid + 1;
        else right = mid - 1;
    }
    if (!found) printf("Student not found.\n");
}

int main() {
    Student students[MAX_STUDENTS];
    int n, choice;
    char target[50];

    readFile(students, &n);

    while (1) {
        printf("\n1. Bubble Sort\n2. Binary Search\n3. Quit\nChoose an option: ");
        scanf("%d", &choice);
        getchar();

        if (choice == 1) {
            bubbleSort(students, n);
            printf("Sorted student records:\n");
            for (int i = 0; i < n; i++)
                printf("%s, %d, %s\n", students[i].name, students[i].rollNo, students[i].department);
        } 
        else if (choice == 2) {
            printf("Enter student name: ");
            fgets(target, sizeof(target), stdin);
            target[strcspn(target, "\n")] = '\0';
            binarySearch(students, n, target);
        } 
        else if (choice == 3) {
            break;
        } 
        else {
            printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}
