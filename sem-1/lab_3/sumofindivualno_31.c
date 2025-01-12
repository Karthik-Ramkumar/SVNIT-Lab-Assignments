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
        store = store + checker;
        input = input / 10; 
    }

    printf("sum of digits: %d\n", store);
    return 0;

}