#include <stdio.h>
#include <stdlib.h>
struct BankMgmt {
    int AccNumber;
    char CustName[30];
    int AvlBalance;
    char AccType[30];
};
int main()
{
    struct BankMgmt bob;
    int choice;
    printf("Enter Account Number: ");
    scanf("%d", &bob.AccNumber);

    printf("Enter Customer Name: ");
    scanf(" %s\n", bob.CustName);

    printf("Enter Available Balance: ");
    scanf("%d", &bob.AvlBalance);

    printf("Enter Account Type: ");
    scanf("%s\n", bob.AccType);  
    
    printf("------------------------------------\n")
    printf("Select option\n");
    printf("1- Withdrawal\n");
    printf("2- Deposit\n");
    printf("3- Display balance\n");
    printf("4- Exit\n");
    printf("------------------------------------\n")
    scanf("%d",&choice);
    while(1)
    {
    switch (choice)
    {
        case 1:
        printf("Enter amount to withdraw:\n");
        int amount;
        scanf("%d",&amount);
        if(amount > bob.AvlBalance)
        {
            bob.AvlBalance -= amount;
            printf("New balance is %d.\n",bob.AvlBalance)
        }
        else {
            printf("Low balance.\n")
        }

        case 2:
        printf("Enter amount to deposit:\n");
        int deposit;
        scanf("%d",&deposit);
        bob.AvlBalance += deposit;

        case 3:
        printf("Account number: %d\n",bob.AccNumber);
        printf("Account name: %d\n",bob.CustName);
        printf("Balance: %d\n",bob.AvlBalance);
        printf("Account type: %d\n",bob.AccType);

        case 4:
        break;

    }
    }
    return 0;

}