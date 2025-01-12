/*    while(input>0)
    {
        checker = input % 10;
        store = store + (checker * i) ;
        i = i * 10;
        input = input/10;
    }
*/
#include <stdio.h>

int main() {
    int input, original, store = 0, checker;
    int i = 1;

    printf("Input number to check whether palindrome or not:\n");
    scanf("%d", &input);

    original = input;

    while (input > 0) {
        checker = input % 10;  // Get the last digit
        store = store * 10 + checker;  // Build the reversed number
        input = input / 10;  // Remove the last digit
    }

    printf("Reversed number: %d\n", store);

    if (store == original) {
        printf("Palindrome number\n");
    } else {
        printf("Not a palindrome number\n");
    }

    return 0;
}
