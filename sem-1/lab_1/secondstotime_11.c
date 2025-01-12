#include <stdio.h>

int main() 
{
    int totalSeconds;
    int hours, minutes, seconds;

    // Reading the total number of seconds
    printf("Enter the total number of seconds: ");
    scanf("%d", &totalSeconds);

    // Calculating hours, minutes, and remaining seconds
    hours = totalSeconds / 3600;                // 1 hour = 3600 seconds
    minutes = (totalSeconds % 3600) / 60;       // 1 minute = 60 seconds
    seconds = totalSeconds % 60;                // Remaining seconds

    // Displaying the result in HH:MM:SS format
    printf("Time is %02d:%02d:%02d\n", hours, minutes, seconds);

    return 0;
}