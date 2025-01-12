#include <stdio.h>

int main() 
{
    float mathMarks, physicsMarks, chemistryMarks, englishMarks;
    float cutoffMark;

    // Reading the marks in Mathematics, Physics, Chemistry, and English
    printf("Enter the marks obtained in Mathematics: ");
    scanf("%f", &mathMarks);

    printf("Enter the marks obtained in Physics: ");
    scanf("%f", &physicsMarks);

    printf("Enter the marks obtained in Chemistry: ");
    scanf("%f", &chemistryMarks);

    printf("Enter the marks obtained in English: ");
    scanf("%f", &englishMarks);

    // Calculating the cutoff mark
    cutoffMark = (mathMarks / 2) + (physicsMarks / 2) + (chemistryMarks / 2) + englishMarks;

    // Displaying the cutoff mark
    printf("The cutoff mark is: %.2f\n", cutoffMark);

    return 0;
}