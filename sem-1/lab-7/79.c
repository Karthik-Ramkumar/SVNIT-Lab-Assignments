#include <stdio.h>

void exchange(int x, int y) 
{
    int temp = x;
    x = y;
    y = temp;
    printf("After swapping x = %d, y = %d\n", x, y);
}

int main() 
{
    int x = 5, y = 10;
    printf("Before swapping x = %d, y = %d\n", x, y);

    exchange(x, y);

    return 0;
}
