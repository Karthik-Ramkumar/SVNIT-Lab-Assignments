//earth time conversion
#include <stdio.h>
    int main()
    {
        float revolution = 31558150;
        float day,hour,minute;
        day = revolution/86400;
        hour = revolution/3600;
        minute = revolution/60;
        printf("number of days = %f", day);
        printf("number of hours = %f", hour);
        printf("number of minutes = %f", minute);
        return 0;
    }