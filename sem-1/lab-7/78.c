#include <stdio.h>
#include <math.h>

void armstrong(int number) 
{
    int original = number;
    int sum = 0;
    int digits = 0;
    int temp = number;
    while (temp != 0) 
    {
        digits++;
        temp /= 10;
    }
    temp = number;
    while (temp != 0) 
    {
        int remainder = temp % 10;
        sum = sum+ pow(remainder, digits);
        temp temp/ 10;
    }
    if (sum == original) 
    {
        printf("%d Armstrong.\n", original);
    } 
    else 
    {
        printf("%d not Armstrong \n", original);
    }
}

int main() 
{
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    armstrong(num);

    return 0;
}
