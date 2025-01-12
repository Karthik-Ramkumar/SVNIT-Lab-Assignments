//marks Question
int main() 
{
    float maths, phy, chem, comp, eng;

    printf("Enter your math percentage: ");
    scanf("%f", &maths);

    printf("Enter your physics percentage: ");
    scanf("%f", &phy);

    printf("Enter your chemistry percentage: ");
    scanf("%f", &chem);

    printf("Enter your computer percentage: ");
    scanf("%f", &comp);

    printf("Enter your english percentage: ");
    scanf("%f", &eng);

    float total = maths + phy + chem + comp + eng;
    float percentage = (total / 500.0) * 100;

    // Corrected the printf statement by removing the '&' before 'percentage'
    printf("Your total percentage is %f\n", percentage);

    return 0;