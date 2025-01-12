//Temperature Question
    #include <stdio.h>

    int main()
    {
        float farh,cels,converter;
        printf("Enter farenheit degree: ");
        scanf("%f",&farh);
        converter = (farh-32)*0.5555;
        printf("your temperature in celsius is %f",converter);
        return 0;
    }