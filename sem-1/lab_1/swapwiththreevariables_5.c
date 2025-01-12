//swapping two variables with third
int main()
 {
    int a = 7;
    int b = 5;
    int c;

    printf("Pattern before swapping: %d %d\n", a, b);

    // Swap using a third variable
    c = a;
    a = b;
    b = c;

    printf("Pattern after switching: %d %d\n", a, b);

    return 0;
}