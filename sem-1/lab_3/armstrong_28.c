#include <stdio.h>
int main()
{
    int input;
    printf("enter your number \n");
    scanf("%d",&input);
    int i, length, checker, cuber, original,temp,adder = 0;
    //storing the original number
    original = input;
    temp = input;
//--------------------------------------------------------------------
    //calculating length of number
    while(temp != 0) 
    {
        temp = temp / 10;
        length++;
    }
//-----------------------------------------------------------------    
    // important step to reinitialize temp to number
    temp = input;
    while (temp != 0) 
    {
        //calculating cubes
        int digit = temp % 10;
        adder += digit * digit * digit;
        temp /= 10;
    }
//--------------------------------------------------------------    
    if(adder == original)
    {
        printf("number is armstrong number");
    }
    
    else
    {
        printf("number is not armstrong number");
    }

    return 0;
    
}