#include <stdio.h>

#define MAX_EMPLOYEES 50
struct Employee 
{
    int employee_number;
    char employee_name[50];
    float basic_pay;
};

int main() 
{
    struct Employee employ[MAX_EMPLOYEES];  
    struct Employee *ptr;
    int n;

    // read number of employees
    printf("Enter the number of employees (<= 50): ");
    scanf("%d", &n);

    // Read employee details
    for (int i = 0; i < n; i++) {
        ptr = &employ[i];  // Point to the current employee in the array

        printf("\nEnter details for employee %d:\n", i + 1);

        printf("Employee Number: ");
        scanf("%d", &ptr->employee_number);
        printf("Employee Name: ");
        getchar();
        gets(ptr->employee_name);
        printf("Basic Pay: ");
        scanf("%f", &ptr->basic_pay);
    }

    // Print details
    printf("\nEmployee List:\n");
    printf("%s %s %s\n", "Emp No.", "Emp Name", "Basic Pay");

    for (int i = 0; i < n; i++) {
        ptr = &employ[i];  
        printf("%d %s %f\n", ptr->employee_number, ptr->employee_name, ptr->basic_pay);
    }

    return 0;
}
