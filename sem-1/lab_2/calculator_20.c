#include <stdio.h>

int main()
{
    int input;
    float a,b,add,sub,multi,div;
    printf("input what action you wanto perform\n");
    printf("1 for addition \n");
    printf("2 for subtraction\n");
    printf("3 for multiplication\n");
    printf("4 for division\n");
    scanf("%d",&input);

    switch(input)
    {
        case 1:
        printf("enter numbers to be added\n");
        scanf("%f%f",&a,&b);
        add = a + b;
        printf("sum is = %f \n",add);
        break;

        case 2:
        printf("enter numbers to be subtracted\n");
        scanf("%f%f",&a,&b);
        sub = a - b;
        printf("subtracted value is = %f \n",sub);
        break;

        case 3:
        printf("enter numbers to be multiplyed\n");
        scanf("%f%f",&a,&b);
        multi = a * b;
        printf("product is = %f \n",multi);
        break;

        case 4:
        printf("enter numbers to be divided\n");
        scanf("%f%f",&a,&b);
        div = a / b;
        printf("quotient is = %f \n",div);
        break;

        default:
        printf("wrong input try again");

    }
    return 0; 
}


    

