#include <stdio.h>
int main()
{
    double i,input1,input2,power;
    printf("enter the number whose power you wanto find\n");
    scanf("%lf",&input1);
    printf("enter the power of the number\n");
    scanf("%lf",&input2);
    i = input2;
    power = input1;
    while(i>1)
    {
        power = power * input1;
        i--;
    }
    printf("power of %lf is = %lf\n",input1,power);
    return 0;
}