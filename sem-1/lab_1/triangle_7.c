//triangle Question

#include <stdio.h>
    int main()
    {
        float base,height,area;
        printf("enter triangle height: ");
        scanf("%f", &height);
        
        printf("enter triangle base: ");
        scanf("%f", &base);
        area = 0.5*base*height;

        printf("your triangle area is %f",area);
        return 0;
    }