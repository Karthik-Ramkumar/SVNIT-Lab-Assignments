#include <stdio.h>
int main()
{
    int square, cube, input, *ptr;
    scanf("%d", &input);
    ptr = &input;
    square = (*ptr) * (*ptr);
    cube = (*ptr) * (*ptr) * (*ptr);
    printf("square = %d \n", square);
    printf("cube = %d \n", cube);
    return 0;
}