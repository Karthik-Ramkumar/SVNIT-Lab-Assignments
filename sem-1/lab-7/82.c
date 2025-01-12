#include <stdio.h>

int factorial(int num) 
{
    int fact = 1;
    for (int i = 1; i <= num; i++) 
    {
        fact *= i;
    }
    return fact;
}
int ncr(int n, int r) 
{
    return factorial(n) / (factorial(r) * factorial(n - r));
}
int main() 
{
    int n, r;
    printf("Enter values for n and r: ");
    scanf("%d %d", &n, &r);
    if (r > n) 
    {
        printf("Invalid input\n");
    } 
    else 
    {
        printf("nCr(%d, %d) = %d\n", n, r, ncr(n, r));
    }
    return 0;
}
