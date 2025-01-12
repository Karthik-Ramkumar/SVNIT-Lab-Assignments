/*#include <stdio.h>
int main()
{
    float even = 0;
    float odd = 0;
    int input;
    int i = 1;
    printf("enter till which number u want sum of odd and even \n");
    scanf("%d",&input);
    while(i <= input)
    {
        odd = odd + i;
        i++;
        even = even+i;
        i++;
    }
    printf("sum of even numbers = %f\n",even);
    printf("sum of odd numbers = %f\n",odd);
    return 0;
}


#include <stdio.h>
int main()
{
    float even = 0;
    float odd = 0;
    int input;  // Change input type to int
    int i = 1;
    printf("Enter till which number you want the sum of odd and even numbers:\n");
    scanf("%d", &input);  // Use %d since input is now an int
    while(i <= input)
    {
        odd = odd + i;
        i++;
        even = even + i;
        i++;
    }
    printf("Sum of even numbers = %f\n", even);
    printf("Sum of odd numbers = %f\n", odd);
    return 0;
}*/

#include <stdio.h>
int main()
{
    float even = 0;
    float odd = 0;
    int input;
    int i = 1;
    printf("Enter till which number you want the sum of odd and even numbers:\n");
    scanf("%d", &input);
    
    while(i <= input)
    {
        odd = odd + i;  // Add to odd sum
        i++;
        if(i <= input)  // Check if still within bounds
        {
            even = even + i;  // Add to even sum
            i++;
        }
    }
    
    printf("Sum of even numbers = %f\n", even);
    printf("Sum of odd numbers = %f\n", odd);
    
    return 0;
}
