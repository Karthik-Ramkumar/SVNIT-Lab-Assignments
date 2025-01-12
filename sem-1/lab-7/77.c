#include <stdio.h>

void palindrome(int num) 
{
    int original = number;
    int reversed = 0;

    // Reverse the number
    while (number != 0)
    {
        int remainder = number % 10;
        reversed = reversed * 10 + remainder;
        number /= 10;
    }

    // Check if the original number is equal to the reversed number
    if (original == reversed) 
    {
        printf("%d is a palindrome.\n", original);
    } else 
    {
        printf("%d is not a palindrome.\n", original);
    }
}

int main() 
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    palindrome(num);

    return 0;
}
