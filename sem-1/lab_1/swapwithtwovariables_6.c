//swapping without third variable
#include <stdio.h>
    int main() 
    {
        int X = 25;
        int Y = 23;

        printf("Before swapping: %d %d\n", X, Y);

        // Swapping without using a third variable
        X = X + Y;
        Y = X - Y;
        X = X - Y;

        printf("After swapping: %d %d\n", X, Y);

        return 0;
    }