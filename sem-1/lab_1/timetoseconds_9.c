#include <stdio.h>

int main() 
{
    int hours, minutes, seconds;
    int total_seconds;

    //Reading time in hours, minutes, and seconds
    printf("Enter hours: ");
    scanf("%d", &hours);

    printf("Enter minutes: ");
    scanf("%d", &minutes);

    printf("Enter seconds: ");
    scanf("%d", &seconds);

    // onverting the time into total seconds
    total_seconds = (hours * 3600) + (minutes * 60) + seconds;

    //Displaying the total number of seconds
    printf("Total time in seconds: %d\n", total_seconds);

    return 0;
}