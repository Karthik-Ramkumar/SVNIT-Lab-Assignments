#include <stdio.h>
int main()
{
     int input, original, store = 0, checker;

    printf("Input number to reverse\n");
    scanf("%d", &input);

    original = input;

    while (input > 0) 
    {
        checker = input % 10;  
        store = store * 10 + checker;  
        input = input / 10;  
    }

    printf("Reversed number: %d\n", store);
    return 0;

}