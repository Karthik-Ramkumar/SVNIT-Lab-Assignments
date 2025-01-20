#include <stdio.h>
#include <string.h>
struct student {
    int rollNo;
    char name[20];
    float marks;
}st;
int main()
{
    int n = 0;
    printf("enter number of students:");
    scanf("%d",&n);
    struct student details[n];
    for (int i = 0; i < n; i++) {
        printf("Enter student %d details:\n", i + 1);
        printf("Roll No: ");
        scanf("%d", &details[i].rollNo); 
        printf("Name: ");
        scanf("%s", details[i].name); 
        printf("Marks: ");
        scanf("%f", &details[i].marks); 
    }
    for (int i = 0; i < n; i++) 
    {
        printf("Details of student %d:\n", i + 1);
        printf("Roll No: %d\n", details[i].rollNo); 
        printf("Name: %s\n", details[i].name); 
        printf("Marks: %.2f\n", details[i].marks); 
    }
    return 0;
}

