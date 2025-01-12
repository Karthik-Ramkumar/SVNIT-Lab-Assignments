//Intrest Question
#include <stdio.h>

int main() {
    int principle, time, rate, interest;

    printf("Enter principle amount: ");
    scanf("%d", &principle);

    printf("Enter time: ");
    scanf("%d", &time);

    printf("Enter rate: ");
    scanf("%d", &rate);

    interest = (principle * time * rate) / 100;
    printf("Your interest amount is %d\n", interest);

    return 0;
}