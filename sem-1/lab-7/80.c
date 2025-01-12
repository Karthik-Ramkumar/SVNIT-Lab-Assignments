#include <stdio.h>

void FIB(int n) 
{
    int a = 0, b = 1, next;
    printf("Fibonacci series for N = %d:\n", n);

    for (int i = 1; i <= n; i++) 
    {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
    printf("\n");
}

int main() 
{
    FIB(5);
    FIB(10);
    FIB(15);

    return 0;
}
