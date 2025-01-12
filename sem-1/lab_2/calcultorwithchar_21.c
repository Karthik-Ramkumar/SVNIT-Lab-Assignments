#include <stdio.h>

int main() 
{
    char input;
    float a, b, add, sub, multi, div;

    printf("Input what action you want to perform\n");
    printf("a for addition\n");
    printf("s for subtraction\n");
    printf("m for multiplication\n");
    printf("d for division\n");
    scanf(" %c", &input);

    switch(input) 
    {
        case 'a':
            printf("Enter numbers to be added\n");
            scanf("%f%f", &a, &b);
            add = a + b;        case 'D':
            printf("Sum is = %f\n", add);
            break;

        case 's':
            printf("Enter numbers to be subtracted\n");
            scanf("%f%f", &a, &b);
            sub = a - b;
            printf("Subtracted value is = %f\n", sub);
            break;

        case 'm':
            printf("Enter numbers to be multiplied\n");
            scanf("%f%f", &a, &b);
            multi = a * b;
            printf("Product is = %f\n", multi);
            break;

        case 'd':
            printf("Enter numbers to be divided\n");
            scanf("%f%f", &a, &b);
            div = a / b;
            printf("Quotient is = %f\n", div);
            break;

        default:
            printf("Wrong input. Try again.\n");
    }

    return 0;
}